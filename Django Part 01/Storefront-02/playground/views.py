from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from store.models import Collection, Customer, Order, Product, OrderItem
from tags.models import TaggedItem

# we can use this to wrap whole function to be a transaction
# @transaction.atomic()
def say_hello(request):
    # try:
    #     query_set = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass

    # query_set = Product.objects.filter(unit_price__range=(20, 30))
    # query_set = Product.objects.filter(collecion__id__range = (1,2,3))
    # query_set = Product.objects.filter(title__icontains="coffee")
    # query_set = Product.objects.filter(last_update__year=2021)
    # query_set = Product.objects.filter(description__isnull=True)

    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # Q class
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # F class
    # query_set = Product.objects.filter(inventory=F("unit_price"))

    # asc
    # c
    # desc
    # query_set = Product.objects.order_by("-title")

    # return a query set
    # query_set = Product.objects.order_by("unit_price", "-title").reverse()

    # return an object
    # product = Product.objects.order_by("unit_price")[0]
    # product = Product.objects.earliest("unit_price")

    # Limiting
    # query_set = Product.objects.all()[:5]
    # limit 5 ofset 5
    # query_set = Product.objects.all()[5:10]

    # selecting fields to query
    # query_set = Product.objects.values("id", "title", "collection__title")
    # query_set = Product.objects.values_list("id", "title", "collection__title")

    # query_set = OrderItem.objects.values("product_id").distinct()
    # query_set = Product.objects.filter(
    #     id__in=OrderItem.objects.values("product_id").distinct()
    # ).order_by("title")

    # defering Fields
    # query_set = Product.objects.only("id", "title")
    # query_set = Product.objects.defer("description")

    # selecting related objects
    # query_set = Product.objects.select_related("collection").all()
    # selecting related objects has many relations
    # query_set = Product.objects.prefetch_related("promotions").all()
    # query_set = (
    #     Product.objects.prefetch_related("promotions")
    #     .select_related("collection")
    #     .all()
    # )
    # query_set = (
    #     Order.objects.select_related("customer")
    #     .prefetch_related("orderitem_set__product")
    #     .order_by("-placed_at")[:5]
    # )

    # aggregation
    # result = Product.objects.aggregate(count=Count("id"), min_price=Min("unit_price"))

    # annotation
    # query_set = Customer.objects.annotate(is_new=Value(True))
    # query_set = Customer.objects.annotate(new_id=F("id") + 1)

    # database function (FUNC)
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )
    # query_set = Customer.objects.annotate(
    #     full_name=Concat("first_name", Value(" "), "last_name")
    # )
    # query_set = Customer.objects.annotate(orders_count=Count("order"))

    # expression wrapper class
    # discounted_price = ExpressionWrapper(
    #     F("unit_price") * 0.8, output_field=DecimalField()
    # )
    # query_set = Product.objects.annotate(discount_price=discounted_price)

    # return render(request, "hello.html", {"name": "KAVEEN", "result": list(query_set)})

    # return render(request, "hello.html", {"name": "KAVEEN", "result": result})

    # return render(request, "hello.html", {"name": "KAVEEN", "orders": list(query_set)})

    # return render(request, "hello.html", {"name": "KAVEEN", "product": product})

    # Querying Generic relations
    # content_type = ContentType.objects.get_for_models(Product)
    # query_set = TaggedItem.objects.select_related("tag").filter(
    #     content_type__model=content_type, object_id=1
    # )

    # Custome Managers
    # query_set = TaggedItem.objects.get_tags_for(Product, 1)
    # return render(request, "hello.html", {"name": "KAVEEN", "tags": list(query_set)})

    # Creating Objects
    # collection = Collection()
    # collection.title = "Video Games"
    # collection.featured_product = Product(pk=1)
    # collection.save()

    # Updating objects
    # this not updating a single field if you remove title field update only feture product framwork set title to null
    # collection = Collection(pk=11)
    # collection.title = "Games"
    # collection.featured_product = None
    # collection.save()

    # Update a single field
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # Deleting objects
    # collection = Collection(pk = 11)
    # collection.delete()
    # Collection(pk=11).objects.filter(id__gt=5).delete()

    # Transactions
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = -1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # sql raw queries
    # queryset = Product.objects.raw("SELECT * FROM store_product")

    # return render(request, "hello.html", {"name": "KAVEEN", "results": list(queryset)})

    return HttpResponse("Hello World")
