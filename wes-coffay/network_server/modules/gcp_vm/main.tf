provider "google" {
  credentials = "${file("~/.ssh/sandbox-fda77da299d1.json")}"
  project     = "sandbox-245021"
  region      = "us-east4"
}

resource "google_compute_instance" "default" {
  name         = "test"
  machine_type = "n1-standard-1"
  zone         = "us-east4-a"

#   tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

#   metadata = {
#     foo = "bar"
#   }

#   metadata_startup_script = "echo hi > /test.txt"

#   service_account {
#     scopes = ["userinfo-email", "compute-ro", "storage-ro"]
#   }
}

# Making the service account and IAM binding
# gcloud projects add-iam-policy-binding sandbox-245021 \
#   --member serviceAccount:terraform@sandbox-245021.iam.gserviceaccount.com \
#   --role roles/compute.admin
