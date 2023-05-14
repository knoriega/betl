from pathlib import Path


JOB_ROOT = Path(__file__).parent
AVAILABLE_JOBS = [
    job.name for job in JOB_ROOT.iterdir()
    if job.is_dir() and job.name != "__pycache__"
]

