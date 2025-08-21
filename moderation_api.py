# pylint: disable=line-too-long, no-member, import-outside-toplevel

import json
import logging
import traceback

import numpy
import detoxify

from django.conf import settings

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

    logger.warning('simple_moderation_detoxify.moderate: %s -- %s', request, moderator)

    try:
        if moderator.moderator_id.startswith('detoxify:'):
            model_name = moderator.moderator_id.replace('detoxify:', '')

            results = detoxify.Detoxify(model_name).predict(request.message)

            logger.warning('simple_moderation_detoxify.moderate.detoxify: %s -- %s -- %s', request, moderator, results)

            json_string = json.dumps(results, indent=2, cls=NumpyEncoder)

            metadata = json.loads(json_string)

            toxicity_threshold = moderator.metadata.get('toxicity_threshold', 0.5)

            if results['toxicity'] < toxicity_threshold:
                return (True, metadata)
            else:
                return (False, metadata)

    except: # pylint: disable=bare-except
        logger.error('simple_moderation_detoxify.moderate ERROR: %s', traceback.format_exc())

    return (None, None)
