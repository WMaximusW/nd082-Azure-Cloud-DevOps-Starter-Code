variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "trungnq72-resource-group-project1"
}

variable "location" {
  description = "The location of the resources"
  type        = string
  default     = "East US"
}

variable "vnet_name" {
  description = "The name of the virtual network"
  type        = string
  default     = "trungnq72-vnet-project1"
}

variable "subnet_name" {
  description = "The name of the subnet"
  type        = string
  default     = "trungnq72-subnet-project1"
}

variable "vm_count" {
  description = "The number of virtual machines to create"
  type        = number
  default     = 3
}

variable "vm_size" {
  description = "The size of the virtual machines"
  type        = string
  default     = "Standard_DS2_v2"
}

variable "admin_username" {
  description = "The admin username for the virtual machines"
  type        = string
}

variable "admin_password" {
  description = "The admin password for the virtual machines"
  type        = string
}

variable "packer_image_name" {
  description = "The name of the Packer image"
  type        = string
  default     = "trungnq72-image-project1"
}

variable "packer_image_resource_group" {
  description = "The resource group where the Packer image is stored"
  type        = string
  default     = "trungnq72-resource-group-project1"
}