#!/usr/bin/env python
import os
import json
import re
from jinja2 import Template


class Route53Generator:
    def __init__(self):
        self.file_path = None
        self.template_path = None
        self.current_dir = "{0}".format(os.curdir)
        self.domain_dir = "{0}/{1}".format(self.current_dir, 'domains')
        self.template_dir = "{0}/{1}".format(self.current_dir, 'templates')
        self.terrvis_dir = "{0}/{1}".format(self.current_dir, '.terrvis')

    def _get_domain_dir(self, domain_dir=None):
        if not domain_dir:
            domain_dir = self.domain_dir
        return domain_dir

    def _get_template_dir(self, template_dir=None):
        if not template_dir:
            template_dir = self.template_dir
        return template_dir

    def get_domain_file_path(self, filename, domain_dir=None):
        self.filename = "{0}/{1}".format(self._get_domain_dir(domain_dir), filename)
        return self.filename

    def get_domain_template_path(self, filename, template_dir=None):
        self.template_filename = "{0}/{1}".format(self._get_template_dir(template_dir), filename)
        return self.template_filename


    def _list_domain_dir(self, domain_dir=None):
        return os.listdir(self._get_domain_dir(domain_dir))

    def load_file(self, filename, domain_dir):
        self.file_path = self.get_domain_file_path(filename, domain_dir)
        try:
            with open(self.file_path) as f:
                return json.load(f)
        except IsADirectoryError as err:
            print("Invalid file: {0}".format(err))
        return ""

    def _generate_terraform_files(self, domain_dir=None):
        domain_regex = re.compile(r"^[a-zA-Z\d-]{,63}(\.[a-zA-Z\d-]{,63}).json$")
        for domain_file in self._list_domain_dir(domain_dir):
            if re.search(domain_regex, domain_file):
                domain_json = self.load_file(domain_file, domain_dir)
                if domain_json:
                    self.write_terraform_template(
                        filename=domain_json['domain'],
                        data=self.render_template(domain_json)
                        )
        return True

    def render_template(self, kwargs, filename='domain.j2', template_dir=None):
        if not template_dir:
            template_dir = self.template_dir
        with open(self.get_domain_template_path(filename, template_dir)) as _file:
            template = Template(_file.read())
            return template.render(**kwargs)

    def write_terraform_template(self, filename, data):
        domain_render_file_path = "{0}/{1}.tf".format(self.terrvis_dir, filename)
        try:
            template_file = open(domain_render_file_path, 'w')
            template_file.write(data)
            template_file.close()
            return True
        except Exception as err:
            print(err)
        return False

    def run(self):
        return self._generate_terraform_files()


if __name__ == '__main__':
    r53 = Route53Generator()
    print(r53.run())
