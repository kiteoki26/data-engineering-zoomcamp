variable "location" {
    description = "PROJECT Location"
    default = "asia"
}

variable "region" {
    description = "Region location"
    default = "asia-southeast1"
}

variable "project" {
    description = "GCP PROJECT NAME"
    default = "dtc-de-course-412407"
}

variable "gcp_bucket_name" {
    description = "Bucket Storage Name"
    default = "dtc-de-course-412407-terrabucket"
}

variable "gcp_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}

variable "credentials" {
    description = "My credentials"
    default = "/key/my_creds.json"
}