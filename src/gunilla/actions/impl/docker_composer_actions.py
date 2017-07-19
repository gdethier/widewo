from gunilla.config import instance
from gunilla.docker import wait_wordpress_container, print_howto
import os
import subprocess


class DockerComposerAction(object):

    def run(self):
        self.change_to_composer_dir()
        self.run_in_composer_dir()

    def change_to_composer_dir(self):
        os.chdir(instance().composer_dir_name())

    def run_composer(self, args):
        command_line = [ 'docker-compose' ]
        command_line.extend(args)
        subprocess.call(command_line)


class Start(DockerComposerAction):

    def run_in_composer_dir(self):
        self.run_composer(['up', '-d'])
        wait_wordpress_container()
        print_howto()


class Stop(DockerComposerAction):

    def run_in_composer_dir(self):
        self.run_composer(['stop'])


class Clear(DockerComposerAction):

    def run_in_composer_dir(self):
        self.run_composer(['stop'])
        self.run_composer(['down', '-v'])
