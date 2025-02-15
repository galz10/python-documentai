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
# Snippet for BatchProcessDocuments
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_v1beta2_generated_DocumentUnderstandingService_BatchProcessDocuments_sync]
from google.cloud import documentai_v1beta2


def sample_batch_process_documents():
    # Create a client
    client = documentai_v1beta2.DocumentUnderstandingServiceClient()

    # Initialize request argument(s)
    requests = documentai_v1beta2.ProcessDocumentRequest()
    requests.input_config.gcs_source.uri = "uri_value"
    requests.input_config.mime_type = "mime_type_value"

    request = documentai_v1beta2.BatchProcessDocumentsRequest(
        requests=requests,
    )

    # Make the request
    operation = client.batch_process_documents(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END documentai_v1beta2_generated_DocumentUnderstandingService_BatchProcessDocuments_sync]
