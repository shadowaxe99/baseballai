```python
import os
import subprocess

def deploy_to_vercel():
    # Ensure the Vercel CLI is installed
    try:
        subprocess.check_call(['vercel', '-v'])
    except subprocess.CalledProcessError:
        print("Vercel CLI not found. Installing...")
        subprocess.check_call(['npm', 'i', '-g', 'vercel'])
    
    # Set up Vercel project
    try:
        subprocess.check_call(['vercel'])
    except subprocess.CalledProcessError:
        print("Failed to set up Vercel project.")
        return

    # Deploy to Vercel
    try:
        subprocess.check_call(['vercel', '--prod'])
    except subprocess.CalledProcessError:
        print("Failed to deploy to Vercel.")
        return

    print("Successfully deployed to Vercel.")

if __name__ == "__main__":
    deploy_to_vercel()
```