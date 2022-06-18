# integrated-project-platform

GCP Set-up:

1. Create bucket: prohost
Permissions:

    Cloud Run Service Agent
    Container Registry Service Agent (i think)
    Give bucket permission to service account - Storage Admin

2. Enable artifact registry API
3. Create repository in artifact registory called 'project-images'
4. Cloud Run permissions:
   1. Service account