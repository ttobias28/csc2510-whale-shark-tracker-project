provider "google" {
  version     = "3.5.0"
  credentials = file("terraform-key.json")
  project     = "whale-shark-devops"
  region      = "us-central1"
  zone        = "us-central1-a"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "f1-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {
      # Ephemeral public IP assigned automatically
    }
  }

  tags = ["whale-shark-app", "http-server"]
}