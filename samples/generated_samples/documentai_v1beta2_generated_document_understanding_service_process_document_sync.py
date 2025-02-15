# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for ProcessDocument
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_v1beta2_generated_DocumentUnderstandingService_ProcessDocument_sync]
from google.cloud import documentai_v1beta2


def sample_process_document():
    # Create a client
    client = documentai_v1beta2.DocumentUnderstandingServiceClient()

    # Initialize request argument(s)
    input_config = documentai_v1beta2.InputConfig()
    input_config.gcs_source.uri = "uri_value"
    input_config.mime_type = "mime_type_value"

    request = documentai_v1beta2.ProcessDocumentRequest(
        input_config=input_config,
    )

    # Make the request
    response = client.process_document(request=request)

    # Handle the response
    print(response)

# [END documentai_v1beta2_generated_DocumentUnderstandingService_ProcessDocument_sync]
