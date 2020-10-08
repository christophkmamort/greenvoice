import os


def brand_branding_upload_path(self, filename):
    brand_name = self.brand.imprint.company_name.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'branding', filename)


def brand_person_upload_path(self, filename):
    # Work on this logic.

    brand_name = self.brand.imprint.company_name.lower().replace(' ', '-')
    person_firstname = self.person.firstname.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'people', person_firstname, 'id_card', filename)
