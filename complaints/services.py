# Standard Library
from collections import defaultdict

# Third Party Stuff
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.db.models import Count

from .models import (
    Complaint , 
    ComplaintComment
)


"""
def get_comments(complaint_id):


    text_questions = get_comment(
        complaint_id=complaint_id)
    choice_questions = get_choice_complaint(
        complaint_id=complaint_id)
    return _merge_questions(text_questions=text_questions,
                            choice_questions=choice_questions)

"""

