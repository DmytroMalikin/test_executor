"""
File contains only the Executor class
"""
import logging
import os
import shlex
import shutil
import subprocess


class Executor:
    """
    Executor class that runs simple pipeline:
    1. Clones a git repository into a working directory
    2. Checks out specific commit hash
    3. Runs the script in the working directory
    4. Cleans up working directory
    """

    def __init__(self, url, commit, argument, workdir='tmp/'):
        """
        Initializes attributes of the executor instance
        :param url: repository url
        :param commit: commit hash
        :param argument: script argument
        :param workdir: name of the working directory. defaults to tmp/
        """
        self.url = url
        self.commit = commit
        self.argument = argument
        self.workdir = workdir
        self.logger = logging.getLogger(__name__)

    def run(self):
        """
        Runs the executor pipeline
        """
        self.logger.info(f'Running an executor with such arguments:\n'
                         f'repo url: {self.url}\n'
                         f'commit hash: {self.commit}\n'
                         f'argument: {self.argument}')

        is_cloned = self.clone()
        if is_cloned:
            self.checkout()
            self.execute()
        self.cleanup()

    def clone(self):
        """
        Tries to clone git repository
        :return: bool - returns True if repository was successfully cloned
        """
        os.mkdir(self.workdir)
        self.logger.info(f'=== STEP 1 ===\nScript workdir {self.workdir} created.')

        try:
            self.logger.info('Cloning a git repository...')
            command = f'git clone {self.url} {self.workdir}'
            subprocess.run(shlex.split(command),
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            self.logger.info('Git repository successfully cloned.')
            return True
        except KeyboardInterrupt:
            self.logger.warning('Cloning canceled.')
            return False

    def checkout(self):
        """
        Checks out the specific commit hash
        """
        self.logger.info('=== STEP 2 ===\nTrying to check out a commit..')
        command = f'git checkout {self.commit}'
        subprocess.run(shlex.split(command),
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       cwd=self.workdir)
        self.logger.info(f'Checked out at {self.commit}.')

    def execute(self):
        """
        Executes script.py from a working directory with given argument
        """
        self.logger.info('=== STEP 3 ===\nTrying to execute script..')
        command = f'python3.7 script.py {self.argument}'
        subprocess.run(shlex.split(command),
                       cwd=self.workdir)
        self.logger.info('Script was successfully executed!')

    def cleanup(self):
        """
        Cleans up temporary working directory
        """
        self.logger.info('=== STEP 4 === \nCleaning up the working directory...')
        shutil.rmtree(self.workdir)
        self.logger.info('Working directory has been cleaned up.')
