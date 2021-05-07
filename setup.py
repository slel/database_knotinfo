from setuptools import setup

def local_scheme(version):
    return ""

setup(
  name = 'database_knotinfo',
  packages = ['database_knotinfo'],
  package_dir  = {'database_knotinfo': 'database_knotinfo'},
  package_data = {'database_knotinfo': ['cvs_data/knotinfo_data_complete.csv',
                                        'cvs_data/linkinfo_data_complete.csv'
                                       ]},
  license='GPL',
  description = 'Content of the KnotInfo and LinkInfo databases as lists of dictionaries',
  author = 'Sebastian Oehms',
  author_email = 'seb.oehms@gmail.com',
  url = 'https://github.com/soehms/database_knotinfo',
  keywords = ['KnotInfo', 'LinkInfo', 'SageMath', 'database'],
  install_requires=[
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
  ],
  include_package_data=True,
  #use_scm_version=True,
  use_scm_version={"local_scheme": local_scheme},
  setup_requires=['setuptools_scm'],
)
