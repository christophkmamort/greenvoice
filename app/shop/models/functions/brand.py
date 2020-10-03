def brand_branding_upload_path(self, filename):
    brand_name = self.name.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'branding', filename)


def brand_person_upload_path(self, filename):
    brand_name = self.name.lower().replace(' ', '-')
    person_firstname = self.firstname.lower().replace(' ', '-')
    return os.path.join('brands', brand_name, 'people', person_firstname, 'id_card', filename)
