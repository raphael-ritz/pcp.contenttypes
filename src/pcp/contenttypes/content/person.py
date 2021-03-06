"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATExtensions import ateapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATBackRef import BackReferenceField
from Products.ATBackRef import BackReferenceWidget

from pcp.contenttypes.interfaces import IPerson
from pcp.contenttypes.config import PROJECTNAME
from pcp.contenttypes.content.common import CommonFields
from pcp.contenttypes.content.common import CommonUtilities


PersonSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    ateapi.FormattableNameField('name',
                                required=1,
                                subfields=('firstnames', 'lastname'),
                                subfield_labels={'firstnames': 'First name(s)',
                                                 'lastname': 'Last name(s)'},
                                ),
    ateapi.EmailField('email',
                      searchable=1,
                      ),
    atapi.ReferenceField('affiliation',
                         relationship='affiliated',
                         allowed_types=('Provider', 'Community'),
                         ),
    ateapi.PhoneNumbersField('phone'),
    BackReferenceField('manages',
                       relationship='managed_by',
                       multiValued=True,
                       widget=BackReferenceWidget(visible={'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('provider_contact_for',
                       relationship='contact',
                       multiValued=True,
                       widget=BackReferenceWidget(label='General contact for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('business_contact_for',
                       relationship='business_contact',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Business contact for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('security_contact_for',
                       relationship='security_contact',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Security contact for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('provider_admin',
                       relationship='admin_of',
                       multiValued=True,
                       widget=BackReferenceWidget(label="Administrator for",
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('she_contact',
                       relationship='contact_for',
                       multiValued=True,
                       widget=BackReferenceWidget(label="SHE contact for",
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('community_contact_for',
                       relationship='community_contact',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Customer contact for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('community_representative',
                       relationship='representative',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Customer representative for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('community_admin',
                       relationship='community_admins',
                       multiValued=True,
                       widget=BackReferenceWidget(label="Customer administrator for",
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('enables',
                       relationship='enabled_by',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Project enabler for',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('service_owner_of',
                       relationship='owned_by',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Service owner of',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('principle_investigator_of',
                       relationship='principal_investigator',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Principle investigator of',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
    BackReferenceField('manager_of_registered_service',
                       relationship='managers_for',
                       multiValued=True,
                       widget=BackReferenceWidget(label='Manager of registered services',
                                                  visible={
                                                      'edit': 'invisible'},
                                                  ),
                       ),
)) + CommonFields.copy()


schemata.finalizeATCTSchema(
    PersonSchema,
    folderish=True,
    moveDiscussion=False
)


class Person(folder.ATFolder, CommonUtilities):
    """Contact details - typically of a person - for a project."""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema


atapi.registerType(Person, PROJECTNAME)
