variable "resource_group_name" {
  type    = string
  default = "az-rg-1"
}

variable "location" {
  type    = string
  default = "uksouth"
}

variable "aks_cluster_name" {
  type    = string
  default = "newlook-cluster"
}

variable "dns_prefix" {
  type    = string
  default = "myaks"
}

variable "node_count" {
  type    = number
  default = 1
}
