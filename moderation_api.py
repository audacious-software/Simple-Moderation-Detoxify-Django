# pylint: disable=line-too-long, no-member, import-outside-toplevel

import json
import logging
import traceback

import numpy
import detoxify

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

from .models import ModerationDecision

class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj): # pylint: disable=arguments-renamed
        if isinstance(obj, numpy.integer):
            return int(obj)

        if isinstance(obj, numpy.floating):
            return float(obj)

        if isinstance(obj, numpy.ndarray):
            return obj.tolist()

        return json.JSONEncoder.default(self, obj)

def moderate(request, moderator):
    logger = logging.getLogger()

    logger.warning('simple_moderation.moderate: %s -- %s', request, moderator)

    try:
        if moderator.moderator_id.startswith('detoxify:'):
            model_name = moderator.moderator_id.replace('detoxify:', '')

            results = detoxify.Detoxify(model_name).predict(request.message)

            logger.warning('simple_moderation.moderate.detoxify: %s -- %s -- %s', request, moderator, results)

            decision = ModerationDecision(request=request, when=timezone.now())

            if results['toxicity'] < settings.SIMPLE_MODERATION_DETOXIFY_THRESHOLD:
                decision.approved = True
            else:
                decision.approved = False

            decision.decision_maker = moderator.moderator_id

            decision.metadata = json.dumps(results, indent=2, cls=NumpyEncoder)

            decision.save()
    except: # pylint: disable=bare-except
        logger.error('simple_moderation.moderate ERROR: %s', traceback.format_exc())

    return (None, None)
