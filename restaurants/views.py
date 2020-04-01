from django.shortcuts import render
from .models import Restaurant
from django.views.generic import ListView


# Create your views here.

class RestaurantList(ListView):
    model = Restaurant
    paginate_by = 10
    template_name = 'homepage/results.html'
    context_object_name = 'all_restaurants'
    
    def apply_cost_rating_filter(self):
         #Check filter-cost. Default value is < 10000
        cost_for_two = int(self.request.GET.get('cost-for-two', 10000))
        
        #By Default restaurants are not filtered by rating
        customer_rating = 0
        ratings_tmp = []
        for rate in range(4, 0, -1):
            if self.request.GET.get("rating-{0}".format(rate), "off") == "on":
                ratings_tmp.append(rate)
        #If no option was selected default to 0
        if ratings_tmp:             
            customer_rating = max(customer_rating, min(ratings_tmp))
        return customer_rating
    
    def resturants_order_by(self):
        # By default resturants are ordered by AggregateRating
        sort_by = 'AggregateRating'
        for sortBy in ["cost", "votes"]:
            if self.request.GET.get('filter-switch-{0}'.format(sortBy), "off") == "on":
                if sortBy == 'cost':
                    sort_by = 'AverageCostForTwo'
                else:
                    sort_by = 'Votes'
        return sort_by
        
    def filter_table_online(self):
         # By default restaurants are not filtered by availability of Online Delivery or Table Booking
        filter_has_table_booking = False
        filter_has_online_delivery = False
        if self.request.GET.get('filter-switch-table', 'off') == "on":
            filter_has_table_booking = True
        if self.request.GET.get('filter-switch-delivery', 'off') == "on":
            filter_has_online_delivery = True
            
        return (filter_has_online_delivery, filter_has_table_booking)
        
    def get_queryset(self):
       customer_rating = self.apply_cost_rating_filter()
       sort_by = self.resturants_order_by()
       filter_has_online_delivery, filter_has_table_booking = self.filter_table_online()
       
        #Apply filters. Remember that django filters are lazy
        all_restaurants = Restaurant.objects.filter(AverageCostForTwo__lte = cost_for_two, AggregateRating__gte = customer_rating).order_by("-"+sort_by)
        if filter_has_table_booking or filter_has_online_delivery:
            if filter_has_table_booking:
                all_restaurants = all_restaurants.filter(HasTableBooking = "Yes")
            if filter_has_online_delivery:
                all_restaurants = all_restaurants.filter(HasOnlineDelivery = "Yes")
        query_item_count = all_restaurants.count()
        
        #Final Queryset created only to split to cuisines. Think if this can be avoided as operetations on database are faster
        final_query_set = [{'rest_id' : obj.RestaurantId, 'name' : obj.RestaurantName, 'currency' : obj.Currency,'has_table' : obj.HasTableBooking, 'has_online' : obj.HasOnlineDelivery, 'rating' : obj.AggregateRating, 'votes' : obj.Votes,  'cost' : obj.AverageCostForTwo, 'cuisines' : list(map(lambda o : o.strip(), obj.Cuisines.split(',')))} for obj in all_restaurants]
        
        return final_query_set
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rest_count'] = len(context['all_restaurants'])
        
        context['costfortwo'] = self.request.GET.get('cost-for-two', 10000)
        for rate in range(4, 0, -1):
            context["rating_{rate}"] = self.request.GET.get('rating-{rate}', "off")
        context["by_cost"] = self.request.GET.get('filter-switch-cost', "off")
        context["by_vote"] = self.request.GET.get('filter-switch-votes', "off")
        context["table_filter"] = self.request.GET.get('filter-switch-table', "off")
        context["delivery_filter"] = self.request.GET.get('filter-switch-delivery', "off")
        
        return context
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        