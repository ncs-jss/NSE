from django.core.mail import EmailMessage
from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@task(name = "send_mail", ignore_result = True)
def send_mail(email):
	"sending signup thanks mail"
	Subject = "Nibble Stock Exchange"
	message = "Thanks for registering on NSE"
	hyperlink = " <a href='http://localhost:8000/nse/'> Nibble Stock Exchange</a>"
	e = EmailMessage(Subject, message + hyperlink, to=[email])
	e.content_subtype = "html"  # Main content is now text/html
	e.send()
	logger.info("mail send")
