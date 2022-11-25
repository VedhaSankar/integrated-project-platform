# integrated-project-platform

GCP Set-up:

1. Create bucket: prohost
2. Permissions for the bucket:

    * Cloud Run Service Agent
    * Container Registry Service Agent (i think)
    * Give bucket permission to service account - Storage Admin

3. Enable artifact registry API
4. Create repository in artifact registory called 'project-images'
5. Cloud Run permissions: Service account
