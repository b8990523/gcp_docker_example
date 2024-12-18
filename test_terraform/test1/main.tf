provider "google" {
  credentials = "${file("mySA.json")}"
  project = "light-team-436602-j3"
  region  = "asia-east1"
}

resource "google_storage_bucket" "quick-start-gcs" {
  name          = "chiayi-gcs-bucket"
  location      = "asia-east1"
  force_destroy = true
}
