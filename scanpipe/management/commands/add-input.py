# SPDX-License-Identifier: Apache-2.0
#
# http://nexb.com and https://github.com/nexB/scancode.io
# The ScanCode.io software is licensed under the Apache License version 2.0.
# Data generated with ScanCode.io is provided as-is without warranties.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# Data Generated with ScanCode.io is provided on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, either express or implied. No content created from
# ScanCode.io should be considered or used as legal advice. Consult an Attorney
# for any legal advice.
#
# ScanCode.io is a free software code scanning tool from nexB Inc. and others.
# Visit https://github.com/nexB/scancode.io for support and download.

from scanpipe.management.commands import ProjectCommand
from scanpipe.management.commands import copy_inputs
from scanpipe.management.commands import validate_inputs


class Command(ProjectCommand):
    help = "Add input files in a project work directory."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "args",
            metavar="input",
            nargs="+",
            help="One or more input file locations.",
        )

    def handle(self, *inputs, **options):
        super().handle(*inputs, **options)

        validate_inputs(inputs)
        copy_inputs(inputs, self.project.input_path)

        msg = (
            f"File(s) copied to the project inputs directory: {self.project.input_path}"
        )
        self.stdout.write(self.style.SUCCESS(msg))