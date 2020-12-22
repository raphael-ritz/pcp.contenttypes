from pcp.contenttypes.comment.comment import CommentField
from pcp.contenttypes.content_dx.common import RequestUtilities
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import implementer


class IServiceComponentRequest(model.Schema):
    """Dexterity Schema for Providers"""

    requested_component = RelationChoice(
        title='Service component',
        description='The service component being requested',
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )
    directives.widget(
        'requested_component',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['servicecomponent_dx'],
            'basePath': make_relation_root_path,
        },
    )

    requested_component_implementations = RelationList(
        title='Implementation',
        description='If only certain implementations are acceptable, this can be specified here. Leave empty if any implementation is fine.',
        default=[],
        value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
        required=False,
        missing_value=[],
    )
    directives.widget(
        'requested_component_implementations',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            'selectableTypes': ['servicecomponentimplementation_dx'],
            'basePath': make_relation_root_path,
        },
    )

    service_hours = RelationChoice(
        title='Service hours',
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )
    directives.widget(
        'service_hours',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['Document'],
            'basePath': make_relation_root_path,
        },
    )

    resource_comment = CommentField(
        comment='If applicable and already known how much resources shall be provisioned '
        'through this service then this should be specified here. Otherwise this '
        'can be left empty (or added later).',
    )


@implementer(IServiceComponentRequest)
class ServiceComponentRequest(Container, RequestUtilities):
    """ServiceComponentRequest instance"""
