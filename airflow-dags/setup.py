# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from setuptools import setup
from setuptools import find_packages

setup(name='Dataproc DAGs',
      version='0.1.0',
      description='Example Airflow DAGs for Google Cloud Dataproc',
      license='APACHE-2.0',
      install_requires=[
          'apache-airflow>=1.9.0',
          'google-api-python-client>=1.7.0'
      ],
      extras_require={
          'tests': [
              'pytest',
              'pytest-pep8',
              'pytest-xdist',
              'pytest-cov'
          ],
      },
      packages=find_packages())
