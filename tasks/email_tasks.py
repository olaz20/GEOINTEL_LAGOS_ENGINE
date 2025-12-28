import smtplib
import logging
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader , select_autoescape
from email.mime.multipart import MIMEMultipart
from core.config import settings
from core.base import celery_app

logger = logging.getLogger(__name__)

env = Environment(
    loader=FileSystemLoader("app/templates"),
    autoescape=select_autoescape(["html", "xml"]),
)

@celery_app.task(bind=True, max_retries=3, default_retry_delay=5)
def send_email_task(
    self,
    subject: str,
    recipient_email: str,
    metadata: dict,
): 
    """
    metadata = {
        "template": "emails/welcome.html",
        "context": {...},
        "text_template": "emails/welcome.txt",  # optional
        "cc": [],
        "bcc": [],
        "reply_to": "support@example.com"
    }
    """
    try:
        template_name = metadata.get("template")
        context = metadata.get("context", {})
        text_template = metadata.get("text_template")
        if not template_name:
            raise ValueError("Email template is required in metadata")
        html_body = env.get_template(template_name).render(context)
        if text_template:
            text_body = env.get_template(text_template).render(context)
        else:
            text_body = "This email requires an HTML-compatible email client."

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = settings.DEFAULT_FROM_EMAIL
        msg["To"] = recipient_email
        if reply_to := metadata.get("reply_to"):
            msg["Reply-To"] = reply_to
        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        recipients = [recipient_email]
        recipients += metadata.get("cc", [])
        recipients += metadata.get("bcc", [])

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(
                settings.SMTP_USERNAME,
                settings.SMTP_PASSWORD,
            )
            server.send_message(
                settings.DEFAULT_FROM_EMAIL,
                recipients,
                msg.as_string(),
            )

        logger.info(f"[Gmail SMTP] Email sent to {recipient_email}")

    except Exception as exc:
        logger.error(f"[Gmail SMTP] Failed: {exc}")
        raise self.retry(exc=exc)
