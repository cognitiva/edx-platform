"""
ACE message types for the instructor module.
"""

from __future__ import absolute_import

from openedx.core.djangoapps.ace_common.message import BaseMessageType


class AccountCreationAndEnrollment(BaseMessageType):
    """
    A message for registering and inviting learners into a course.

    This message includes username and password.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(AccountCreationAndEnrollment, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class AddBetaTester(BaseMessageType):
    """
    A message for course beta testers when they're invited.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(AddBetaTester, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class AllowedEnroll(BaseMessageType):
    """
    A message for _unregistered_ learners who received an invitation to a course.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(AllowedEnroll, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class AllowedUnenroll(BaseMessageType):
    """
    A message for _unregistered_ learners who had their invitation to a course cancelled.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(AllowedUnenroll, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class EnrollEnrolled(BaseMessageType):
    """
    A message for _registered_ learners who have been both invited and enrolled to a course.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(EnrollEnrolled, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class EnrolledUnenroll(BaseMessageType):
    """
    A message for _registered_ learners who have been unenrolled from a course.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(EnrolledUnenroll, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation


class RemoveBetaTester(BaseMessageType):
    """
    A message for course beta testers when they're removed.
    """
    APP_LABEL = 'instructor'

    def __init__(self, *args, **kwargs):
        super(RemoveBetaTester, self).__init__(*args, **kwargs)
        self.options['transactional'] = True  # pylint: disable=unsupported-assignment-operation
