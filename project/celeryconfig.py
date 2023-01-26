CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
result_backend = 'redis://localhost:6379'

# json serializer is more secure than the default pickle

accept_content = ['json']
result_serializer = 'json'

# Use UTC instead of localtime
CELERY_ENABLE_UTC = True

# Maximum retries per task
CELERY_TASK_ANNOTATIONS = {'*': {'max_retries': 3}}

# A custom property used in tasks.py:run()
CUSTOM_RETRY_DELAY = 10
# options --------------------------------------------------


# task_annotations = {"tasks.add": {"rate_limit": "10/m"}} #برای تسک های سنگین یعنی مثلا هر دقیقه 10 بار حداقل اجرا شه
# task_routes = {"emailNotification.tasks.add": "low-priority"}
task_routes = {
                "emailNotification.tasks.simpleTask.add": {"queue": "queue1"},
                "emailNotification.tasks.simpleTask.average": {"queue": "queue2"},
                "emailNotification.tasks.simpleTask.sum": {"queue": "queue3"}
                }

# include = [ "project.tasks"] # نشون میده تسک هارو از کجا بخونه