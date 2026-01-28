variable "subscription_id" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "client_id" {
  type = string
}

variable "client_secret" {
  type      = string
  sensitive = true

}

variable "resource_group_name" {
  type    = string
  default = "aks-microservices-rg"
}

variable "location" {
  type    = string
  default = "canadacentral"
}

variable "aks_name" {
  type    = string
  default = "microservices-aks"
}

variable "acr_name" {
  type = string
}

variable "dns_prefix" {
  type    = string
  default = "microaks"
}

variable "node_count" {
  type    = number
  default = 1
}

variable "vm_size" {
  type    = string
  default = "standard_a2_v2"
}