class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if not hasattr(self,"_name"):
            if type(new_name) == str and 1 <= len(new_name) <= 15:
                self._name = new_name
    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        all_visitors = [trip.visitor for trip in self.trips()]
        return max(all_visitors, key=all_visitors.count)


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,new_start_date):
        if type(new_start_date) == str and 7 <= len(new_start_date):
            self._start_date = new_start_date
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self,new_end_date):
        if type(new_end_date) == str and 7 <= len(new_end_date):
            self._end_date = new_end_date
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self,new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,new_national_park):
        if isinstance(new_national_park,NationalPark):
            self._national_park = new_national_park
class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self ]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        pass