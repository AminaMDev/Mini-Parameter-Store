# Mini Parameter Store

To see how you approach software development in an environment like ours, we'd like you to implement a simple parameter store accessible via a REST API.

You can pick your technologies, but we're a Python/Django shop, so we thought of the problem that way.  Just be ready to talk about why you picked the tools you did.

We're targeting this at around a 2 hour project.  If it's taking significantly longer, reach out to us-- we can always work with an in progress project for this discussion.

## Requirements

1. Provide a single API endpoint with the usual REST commands (POST/PATCH/PUT/GET/DELETE) for parameters.
1. Each parameter has a name, a value, and an indication whether or not it is a secret.
1. If a parameter is a secret, it should not be stored in plaintext

### Things Not to Worry About

* Don't spend a lot of time on how you avoid storing in plaintext-- anything is fine, we're more interested in how you approach the decision to encrypt/decrypt.
* Don't worry about users and auth, you can just skip it for this project or use something super simple.
* You don't have to worry about scalability, real world deployment models, etc.  The code is what we're interested in seeing.

### Things TO Worry About

* We view this as a chance for you to show off how you code, do the work like you would if it's your day job.
* Be sure to include documentation on how to run and test your project.

## Submission

Organize the code as you would production, include any necessary documentation and push to the `master` branch.
