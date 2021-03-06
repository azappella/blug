from distutils.core import setup
import distutils.command.install_scripts
import shutil

class ScriptInstaller (distutils.command.install_scripts.install_scripts):
    def run(self):
        distutils.command.install_scripts.install_scripts.run(self)
        for script in self.get_outputs():
            if script.endswith(".py"):
                shutil.move(script, script[:-3])

setup(
    name = 'blug',
    scripts = ['blug.py'],
    version = '0.1.0',
    cmdclass = {"install_scripts": ScriptInstaller },
    description = 'Static site generator for Markdown based blogs, with a built-in webserver',
    author = 'Jeff Knupp',
    author_email = 'jknupp@gmail.com',
    url = 'http://www.github.com/jeffknupp/blug',
    keywords = ['blog', 'markdown', 'static', 'website', 'generator'],
    requires = ['Jinja2 (>=2.6)', 'Markdown (>=2.2.0)', 'PyYAML (>=3.10)'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Text Processing :: Markup',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    long_description = '''\
Blug - The Opinionated Static Blog Generator
--------------------------------------------

Blug is *another* static blog generator for blog posts written in Markdown.
The current styling is directly taken from the Octopress default theme, though
this will change shortly. It includes a built-in
webserver for previewing posts.

Blug is on Github at http://www.github.com/jeffknupp/blug
'''
)
