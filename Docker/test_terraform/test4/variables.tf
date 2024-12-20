variable "GCP_PROJECT" {
  description = "The GCP Project ID"
  default     = "light-team-436602-j3"
}

variable "GCP_CREDENTIALS" {
  description = "Path to the GCP service account key file"
  default     = "mySA.json"
}


variable "GCP_REGION" {
  type    = string
  default = "asia-east1"
}

variable "db_name" {
  type    = string
  default = "mydb2"
}
