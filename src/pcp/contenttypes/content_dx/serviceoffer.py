## -*- coding: UTF-8 -*-
from collective import dexteritytextindexer
from plone import api
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer

class IServiceOffer(model.Schema):
    """Dexterity Schema for ServiceOffer
    """

    service = RelationChoice(
        title=u"Service offered",
        description=u"Reference to the catalog entry of the service being offered.",
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )   
    directives.widget(
        "service",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["service_dx"],
            "basePath": make_relation_root_path,
        },
    )

    service_option = RelationChoice(
        title=u"Service option offered",
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )   
    directives.widget(
        "service_option",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["Document"],
            "basePath": make_relation_root_path,
        },
    )

    slas = RelationList(
        title=u"SLAs offered",
        description=u"Potential Service Level Agreements under which the service is being offered.",
        default=[],
        value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
        required=False,
        missing_value=[],
    )
    directives.widget(
        "slas",
        RelatedItemsFieldWidget,        
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            "selectableTypes": ["Document"],
            "basePath": make_relation_root_path,
        },
    )

    contact = RelationChoice(
        title=u"Contact",
        description=u"Contact responsible for this service offer.",
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )   
    directives.widget(
        "contact",
        RelatedItemsFieldWidget,
        pattern_options={
            "selectableTypes": ["person_dx"],
            "basePath": make_relation_root_path,
        },
    )

@implementer(IServiceOffer)
class ServiceOffer(Container):
    """ServiceOffer instance"""