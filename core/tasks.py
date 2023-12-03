from celery import shared_task

from django.core.files.storage import default_storage
from django.http import response
from django.utils import timezone
from django.views import View

from core.models import InformationModel
from core.views import html_to_pdf


@shared_task
def delete_old_pdf(file_path):
    # Calculate the timestamp for 1 hour ago
    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)

    # Get the file's modification time
    file_modified_time = default_storage.get_modified_time(file_path)

    # If the file was modified more than 1 hour ago, delete it
    if file_modified_time < one_hour_ago:
        try:
            default_storage.delete(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


class PDFView(View):
    def get(self, request, *args, **kwargs):
        # Getting all information data
        context = {
            "infos": InformationModel.objects.all()
        }
        pdf = html_to_pdf('core/main.html', context)

        # Close the PDF object cleanly and we're done.
        pdf.showPage()
        pdf.save()

        # Schedule the Celery task to delete the file after 1 hour
        file_path = 'home/ajay/Downloads/download.pdf'
        delete_old_pdf.apply_async(args=[file_path], countdown=3600)  # Countdown is in seconds

        return response
