from django.db import models
import uuid


class PurchaseOrderHeader(models.Model):
    tenant_organisation = models.IntegerField()
    po_number = models.CharField("PO Number", max_length=32)
    business_partner = models.IntegerField()
    STATUS_CHOICES = (
        ('1', 'registered'),
        ('2', 'approved'),
        ('3', 'confirmed'),
        ('4', 'cancelled'),
        ('5', 'delivered')
    )
    status = models.CharField(
        "Status",
        max_length=1,
        null=False,
        blank=False,
        choices=STATUS_CHOICES
    )
    delivery_date = models.DateField("Delivery Date")
    total_value = models.IntegerField("Total Value")
    weight = models.IntegerField("Weight", null=True, blank=True)
    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)

    def __str__(self):
        return f"PurchaseOrder({self.id}, {self.po_number})"


class BusinessPartner(models.Model):
    name = models.CharField("Name", max_length=64)
    email = models.EmailField("Email")
    mobile = models.CharField("Mobile no", max_length=10)
    PARTNER_CATEGORY = (
        ('1', 'person'),
        ('2', 'organization'),
        ('3', 'group')
    )
    partner_category = models.CharField(
        "Partner",
        max_length=1,
        null=False, 
        choices=PARTNER_CATEGORY
    )
    organisation = models.IntegerField()
    gst_number = models.CharField("GST Number", max_length=64)
    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Modified", auto_now=True)	

    def __str__(self):
        return f"{self.name}"


class Organisation(models.Model):
    tenant = models.IntegerField()
    name = models.CharField(max_length=64)
    gst_number = models.CharField(max_length=64)
    description = models.TextField(null=True)
    STATUS_CHOICES = (
        ('1', 'Active'),
        ('2', 'Expired'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )


class Tenant(models.Model):
    tenant_code = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=64)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    domain = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True)
    STATUS_CHOICES = (
        ('1', 'Active'),
        ('2', 'Expired'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name