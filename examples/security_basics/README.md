# Supplied security examples

Course reading: [Big Data Search and Security](https://vibhug0077.github.io/Big_Data_Search_Security/).

Run the dependency-free integrity and role-based access examples:

```powershell
docker compose -f docker/course-dev/docker-compose.yml run --rm course-dev `
  bash -lc "cd /tmp && python3 /workspace/examples/security_basics/code/tampering_example.py && python3 /workspace/examples/security_basics/code/role_based_access.py"
```

Kafka configuration examples are retained with the Chapter 7 Kerberos
material because they require a configured broker, credentials, and
certificates. Do not treat platform-dependent source files as tested
deployments.
