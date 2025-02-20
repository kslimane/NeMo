# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
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

import os

try:
    import pynini

    PYNINI_AVAILABLE = True
except (ImportError, ModuleNotFoundError):
    PYNINI_AVAILABLE = False


def parse_test_case_file(file_name: str):
    """
    Prepares tests pairs for ITN and TN tests
    """
    test_pairs = []
    with open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + file_name, 'r') as f:
        for line in f:
            spoken, written = line.split('~')
            test_pairs.append((spoken, written.strip("\n")))
    print(test_pairs)
    return test_pairs


def get_test_cases_multiple(file_name: str = 'data_text_normalization/test_cases_normalize_with_audio.txt'):
    """
    Prepares tests pairs for audio based TN tests
    """
    test_pairs = []
    with open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + file_name, 'r') as f:
        for line in f:
            written, normalized_options = line.split('~')
            normalized_options = normalized_options.strip().split('|')
            test_pairs.append((written, normalized_options))
    return test_pairs
