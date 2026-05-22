# Deployment and Hosting Guide

This guide describes how to deploy the SDC Networks backend (Django REST API + PostgreSQL) to **DigitalOcean App Platform** and connect it to your frontend hosted on **Vercel**.

---

## Architecture Overview
* **Frontend**: Next.js hosted on **Vercel** (`https://www.sdcnetworks.com`).
* **Backend**: Django REST Framework hosted on **DigitalOcean App Platform**.
* **Database**: Managed **PostgreSQL** provided on DigitalOcean.
* **Media Storage**: **Cloudinary** (essential for production since hosting containers are stateless and local files will be deleted on server restarts).

---

## 1. Cloudinary Setup (Media Storage)
Before deploying, make sure you have your Cloudinary credentials ready:
1. Log in to [Cloudinary](https://cloudinary.com/).
2. From the dashboard console, note your:
   * **Cloud Name**
   * **API Key**
   * **API Secret**
3. Ensure these credentials have full write permissions (`create` actions allowed).

---

## 2. Backend Deployment on DigitalOcean App Platform

Using the included `app.yaml` configuration, you can deploy your Django API backend and PostgreSQL database together on the DigitalOcean App Platform.

### Setup Steps
1. Log in to the [DigitalOcean Control Panel](https://cloud.digitalocean.com/).
2. Click **Apps** in the left sidebar, then click **Create App**.
3. Select **GitHub** as the source, choose your backend repository (`Sdc-Backend-`), and select your deployment branch (e.g. `main`).
4. Click **Next**. DigitalOcean will automatically detect the `app.yaml` file at the root of the repository and configure the components:
   * **sdc-backend** (Python/Django Web Service)
   * **sdc-db** (Managed PostgreSQL database)
5. On the **Resources** or **Environment Variables** configuration step:
   - Click on the **sdc-backend** service and enter values for the missing secrets:
     * `SECRET_KEY`: Enter a long, secure random string.
     * `CLOUDINARY_API_KEY`: Your Cloudinary API Key.
     * `CLOUDINARY_API_SECRET`: Your Cloudinary API Secret.
6. Review the specs and click **Create Resources** to build and launch your backend API.
7. Once deployed, DigitalOcean will provide a domain name for your backend (e.g. `https://sdc-backend-xxxxx.ondigitalocean.app/`). Copy this URL.

---

## 3. Connecting Frontend (Vercel) to Backend

To link your Vercel frontend with the new DigitalOcean backend API:

1. Log in to the [Vercel Dashboard](https://vercel.com/) and open your project.
2. Go to **Settings** -> **Environment Variables**.
3. Add or update the following environment variable:
   * **Key**: `NEXT_PUBLIC_API_URL`
   * **Value**: `https://sdc-backend-xxxxx.ondigitalocean.app` *(Your DigitalOcean App URL)*
4. Go to **Deployments** in Vercel and **Redeploy** the latest commit so that the new API URL is built into your Next.js application.

---

## 4. Database Seeding in Production

To populate your DigitalOcean PostgreSQL database with the initial courses, trainers, and placement student records:

1. Retrieve the **production database connection URL** (e.g., the external PostgreSQL Connection String from the `sdc-db` component in the DigitalOcean dashboard).
2. On your local machine, open `backend/.env` and temporarily replace the `DATABASE_URL` with the production database URL:
   ```env
   DATABASE_URL=postgresql://your-prod-db-url
   ```
   Ensure your correct Cloudinary environment variables are also set in the local `backend/.env` file.
3. In your local terminal, navigate to the `backend` folder and run the seed scripts:
   ```bash
   # Make sure your virtual env is active
   python seed_courses.py
   python seed_trainers.py
   python seed_placements.py
   ```
4. **Important**: Since your local media files (images) exist on your computer, running the seed scripts locally with the production database active will upload all images to your production Cloudinary account and save the Cloudinary URLs directly to the production database!
5. Once completed, revert your local `DATABASE_URL` back to SQLite/local config to avoid accidentally overwriting production data in the future.
