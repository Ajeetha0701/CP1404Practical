class Project:
    def __init__(self, name, start_date_str, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date_str = start_date_str
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def compare_date_with_input_date(self, input_date):
        project_date = datetime.datetime.strptime(self.start_date_str, "%d/%m/%y").date()
        return project_date > input_date

    def __str__(self):
        return f"{self.name}, Start Date: {self.start_date_str}, Priority: {self.priority}, " \
               f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}%"
