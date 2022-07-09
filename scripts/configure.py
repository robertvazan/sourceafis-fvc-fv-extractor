# This script generates and updates project configuration files.

# We are assuming that project-config is available in sibling directory.
# Checkout from https://github.com/robertvazan/project-config
import pathlib
project_directory = lambda: pathlib.Path(__file__).parent.parent
config_directory = lambda: project_directory().parent/'project-config'
exec((config_directory()/'src'/'net.py').read_text())

root_namespace = lambda: 'SourceAFIS.Fvc.FV.Extractor'
pretty_name = lambda: 'SourceAFIS extractor for FVC FV'
subdomain = lambda: 'sourceafis'
homepage = lambda: website() + 'fvc'
inception_year = lambda: 2022
is_library = lambda: False
assembly_name = lambda: 'enroll'
has_website = lambda: False
md_description = lambda: '''\
	Submission of [SourceAFIS](https://sourceafis.machinezoo.com/) extractor
	to [Fingerprint Verification](https://biolab.csr.unibo.it/FVCOnGoing/UI/Form/BenchmarkAreas/BenchmarkAreaFV.aspx) benchmark
	in [FVC-onGoing](https://biolab.csr.unibo.it/FVCOnGoing/UI/Form/Home.aspx) competition.
'''

def documentation_links():
    yield 'SourceAFIS overview', 'https://sourceafis.machinezoo.com/'

def dependencies():
    use('SourceAFIS:3.14.0')

generate()
