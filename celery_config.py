from kombu import Queue

task_routes = ([
    ('step1.s1', {'queue': 'step1_tasks',
                         'routing_key': 'step1.s1'}),
    ('step2.s2', {'queue': 'step2_tasks',
                          'routing_key': 'step2.s2'}),
],)
task_queues = (
    Queue('step1_tasks', routing_key='step1.#'),
    Queue('step2_tasks', routing_key='step2.#'),
)
