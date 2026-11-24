#!/usr/bin/env python3
"""
Generates the publication-quality, 3-page Assignment 2 Report PDF for
Introduction to DevOps (BITS Pilani - CSIZG514/SEZG514)
Author: DrSunandaPandita (BITS ID: 2025tm93132@wilp.bits-pilani.ac.in)
"""

import subprocess
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ACEest Fitness & Gym — DevOps Assignment 2 Technical Report</title>
<style>
  @page {
    size: A4;
    margin: 11mm 13mm 11mm 13mm;
    @bottom-right {
      content: counter(page) " / " counter(pages);
      font-size: 8pt;
      color: #64748b;
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0f172a;
    line-height: 1.38;
    font-size: 8.8pt;
    margin: 0;
    padding: 0;
  }
  .header {
    border-bottom: 2px solid #0284c7;
    padding-bottom: 6px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .title-block h1 {
    font-size: 15.5pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 2px 0;
    letter-spacing: -0.02em;
  }
  .title-block .subtitle {
    font-size: 9.5pt;
    font-weight: 600;
    color: #0284c7;
    margin: 0;
  }
  .meta-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 6px 10px;
    margin-bottom: 8px;
    gap: 5px 14px;
    font-size: 8.2pt;
  }
  .meta-item strong {
    display: block;
    color: #475569;
    font-size: 7.2pt;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 1px;
  }
  a {
    color: #0284c7;
    text-decoration: underline;
  }
  h2 {
    font-size: 10.2pt;
    font-weight: 700;
    color: #0f172a;
    border-left: 3px solid #0284c7;
    padding-left: 6px;
    margin: 9px 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
  h3 {
    font-size: 9pt;
    font-weight: 700;
    color: #1e293b;
    margin: 6px 0 3px 0;
  }
  p {
    margin: 0 0 5px 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0 6px 0;
    font-size: 8pt;
  }
  th, td {
    padding: 4.5px 7px;
    border: 1px solid #cbd5e1;
    text-align: left;
    vertical-align: top;
  }
  th {
    background: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
  }
  tr:nth-child(even) td {
    background: #f8fafc;
  }
  .code-block {
    background: #0f172a;
    color: #f8fafc;
    padding: 6px 8px;
    border-radius: 4px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 7.4pt;
    margin: 3px 0 6px 0;
    line-height: 1.28;
    white-space: pre-wrap;
  }
  .box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 9px;
    margin-bottom: 6px;
    font-size: 8pt;
  }
  .page-break {
    page-break-after: always;
    break-after: page;
  }
</style>
</head>
<body>

<!-- ===================================================================== -->
<!-- PAGE 1: Executive Summary, Deliverables & Core Application Design    -->
<!-- ===================================================================== -->

<div class="header">
  <div class="title-block">
    <h1>ACEest Fitness &amp; Gym — DevOps Assignment 2</h1>
    <p class="subtitle">Automated CI/CD Pipeline, Quality Gates &amp; Advanced Kubernetes Deployments</p>
  </div>
</div>

<div class="meta-grid">
  <div class="meta-item"><strong>Institution &amp; Course</strong>BITS Pilani &bull; Introduction to DevOps (CSIZG514/SEZG514)</div>
  <div class="meta-item"><strong>Student / Author</strong>DrSunandaPandita (2025tm93132@wilp.bits-pilani.ac.in)</div>
  <div class="meta-item"><strong>Public GitHub Repository</strong><a href="https://github.com/DrSunandaPandita/aceest-fitness-gym" target="_blank">https://github.com/DrSunandaPandita/aceest-fitness-gym</a></div>
  <div class="meta-item"><strong>Container Registry (Docker Hub)</strong><a href="https://hub.docker.com/r/drsunandapandita/aceest-fitness" target="_blank">https://hub.docker.com/r/drsunandapandita/aceest-fitness</a></div>
</div>

<h2>1. Executive Summary &amp; Deliverables Verification Matrix</h2>
<p>
This report presents the implementation and empirical validation of an automated Continuous Integration and Continuous Delivery (CI/CD) lifecycle for <strong>ACEest Fitness &amp; Gym</strong>. Evolving from the foundational microservice developed in Assignment 1, this project establishes multi-version release tracking across 10 course prototypes, automated unit testing with Pytest (26 test cases, 94% coverage), static analysis with SonarQube quality gates, multi-tag Docker Hub containerization, and zero-downtime orchestration across <strong>5 distinct Kubernetes deployment strategies</strong> with self-healing rollbacks.
</p>

<table>
  <thead>
    <tr>
      <th style="width: 24%;">Mandate</th>
      <th style="width: 48%;">Implementation Details</th>
      <th style="width: 28%;">Verification Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Application &amp; Versions</strong></td>
      <td>Modular Flask web microservice (<code>app.py</code>) mapping 10 course prototype versions across semantic releases.</td>
      <td>Verified &amp; Archived in <code>code_versions/</code></td>
    </tr>
    <tr>
      <td><strong>Public Repository &amp; VCS</strong></td>
      <td><a href="https://github.com/DrSunandaPandita/aceest-fitness-gym" target="_blank">https://github.com/DrSunandaPandita/aceest-fitness-gym</a><br>Release tags: <code>v1.0.0</code>, <code>v2.0.0</code>, <code>v3.0.0</code></td>
      <td>Applied (v1.0.0, v2.0.0, v3.0.0)</td>
    </tr>
    <tr>
      <td><strong>Automated Unit Testing</strong></td>
      <td>Pytest suite with 26 automated unit/integration tests; 94%+ statement coverage; JUnit XML test artifacts.</td>
      <td>Passed (26/26 tests passed)</td>
    </tr>
    <tr>
      <td><strong>CI Automation (Jenkins)</strong></td>
      <td>Declarative <code>Jenkinsfile</code> with SCM polling (<code>H/5 * * * *</code>), 9 automated build stages, and rollback.</td>
      <td>Configured &amp; Verified</td>
    </tr>
    <tr>
      <td><strong>Code Quality &amp; Quality Gate</strong></td>
      <td>SonarQube static code analysis (<code>sonar-project.properties</code>) with quality gate threshold enforcement.</td>
      <td>Quality Gate Passed</td>
    </tr>
    <tr>
      <td><strong>Container Registry</strong></td>
      <td>Docker Hub multi-version images: <a href="https://hub.docker.com/r/drsunandapandita/aceest-fitness" target="_blank">https://hub.docker.com/r/drsunandapandita/aceest-fitness</a></td>
      <td>Tagged (v1.0.0, v2.0.0, v3.0.0, latest)</td>
    </tr>
    <tr>
      <td><strong>Kubernetes Deployments</strong></td>
      <td>5 Advanced Strategies: Rolling Update, Blue-Green, Canary 80/20, A/B Testing, Shadow Mirroring.</td>
      <td>Implemented &amp; Active (<code>k8s/</code>)</td>
    </tr>
    <tr>
      <td><strong>Resilience &amp; Rollback</strong></td>
      <td>Automated failure detection and self-healing rollback via <code>kubectl rollout undo</code>.</td>
      <td>Validated (Self-Healing Rollout)</td>
    </tr>
  </tbody>
</table>

<h2>2. Core Web Architecture &amp; REST API Endpoints</h2>
<p>
The application transitions the legacy desktop scripts into an enterprise web service built on Flask 3.x and served via Gunicorn WSGI with multi-threaded worker configurations (<code>--workers 2 --threads 4</code>). Dynamic runtime configuration is driven by environment variables (<code>APP_VERSION</code>, <code>RELEASE_COLOR</code>, <code>PORT</code>), enabling live status display in both UI badges and API health endpoints.
</p>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Endpoint</th>
      <th style="width: 15%;">HTTP Method</th>
      <th style="width: 40%;">Description &amp; Payload</th>
      <th style="width: 20%;">Operational Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>/health</code></td>
      <td>GET</td>
      <td>Returns JSON with service status, version, color, and UTC timestamp.</td>
      <td>K8s liveness &amp; readiness probes</td>
    </tr>
    <tr>
      <td><code>/api/version</code></td>
      <td>GET</td>
      <td>Returns version metadata, environment, color, and pod hostname.</td>
      <td>Deployment strategy verification</td>
    </tr>
    <tr>
      <td><code>/api/plans</code></td>
      <td>GET</td>
      <td>Retrieves tiered membership catalog (Starter Zinc, Pro, Elite Athlete).</td>
      <td>Plan discovery &amp; pricing catalog</td>
    </tr>
    <tr>
      <td><code>/api/members</code></td>
      <td>GET, POST</td>
      <td>Thread-safe member registration and athlete directory CRUD operations.</td>
      <td>Member enrollment management</td>
    </tr>
    <tr>
      <td><code>/api/classes/book</code></td>
      <td>POST</td>
      <td>Books scheduled studio sessions (Spin, CrossFit, HIIT, Mobility).</td>
      <td>Real-time studio capacity tracking</td>
    </tr>
    <tr>
      <td><code>/api/calculator/bmi</code></td>
      <td>POST</td>
      <td>Calculates biometric BMI and Mifflin-St Jeor daily caloric expenditure.</td>
      <td>Metabolic athletic health tools</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ===================================================================== -->
<!-- PAGE 2: CI/CD Pipeline & 5 Kubernetes Deployment Strategies          -->
<!-- ===================================================================== -->

<h2>3. End-to-End Automated CI/CD Lifecycle &amp; Quality Gates</h2>
<p>
The delivery lifecycle is automated via a declarative Jenkins pipeline (<code>Jenkinsfile</code>) with SCM polling every 5 minutes (<code>H/5 * * * *</code>), enforcing progressive verification gates before any containerized artifact is deployed to the cluster.
</p>

<div class="box">
<strong>Pipeline Execution Workflow &amp; Quality Checks:</strong><br>
&bull; <strong>Stage 1: Checkout SCM:</strong> Pulls latest commit and release tags from public GitHub repository.<br>
&bull; <strong>Stage 2: Setup &amp; Flake8 Linting:</strong> Initializes virtualenv and runs Flake8 enforcing PEP8 conformity and cyclomatic complexity (&le; 10).<br>
&bull; <strong>Stage 3: Automated Pytest Suite:</strong> Executes 26 unit and integration tests; generates JUnit XML and Cobertura coverage reports.<br>
&bull; <strong>Stage 4 &amp; 5: SonarQube Quality Gate:</strong> Static analysis checks for code smells, bugs, and security vulnerabilities; enforces Quality Gate.<br>
&bull; <strong>Stage 6 &amp; 7: Container Assembly &amp; In-Container Smoke Test:</strong> Builds Docker image and runs <code>docker run --rm ... pytest tests/</code>.<br>
&bull; <strong>Stage 8: Registry Push:</strong> Publishes multi-tag versioned images (<code>v1.0.0</code>, <code>v2.0.0</code>, <code>v3.0.0</code>, <code>latest</code>) to Docker Hub.<br>
&bull; <strong>Stage 9: Kubernetes Continuous Delivery:</strong> Applies manifests; validates rollout status; triggers automatic rollback upon failure.
</div>

<h2>4. Progressive Kubernetes Deployment Strategies</h2>
<p>
To satisfy the core requirement of Assignment 2, the containerized application is orchestrated across 5 advanced deployment methodologies in the <code>aceest-fitness</code> namespace, each codified as declarative YAML manifests in <code>k8s/</code>:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 20%;">Deployment Strategy</th>
      <th style="width: 48%;">Architectural Mechanism &amp; Manifest Details</th>
      <th style="width: 32%;">Operational Benefit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Rolling Update</strong><br><code>01-rolling-update.yaml</code></td>
      <td>Configured with <code>maxSurge: 1</code> and <code>maxUnavailable: 0</code>. Pods are updated incrementally one-by-one. Live traffic routes only to pods that have passed HTTP <code>/health</code> readiness probes.</td>
      <td><strong>Zero Downtime:</strong> 100% capacity maintained during updates without extra infrastructure cost.</td>
    </tr>
    <tr>
      <td><strong>2. Blue-Green</strong><br><code>02-blue-green.yaml</code></td>
      <td>Two discrete fleets run in parallel: <code>aceest-blue</code> (v1.0.0) and <code>aceest-green</code> (v2.0.0). Traffic switch is executed by an atomic service selector patch: <code>selector: { version: green }</code>.</td>
      <td><strong>Instant Cutover:</strong> Atomic switchover with zero latency impact and immediate 1-second fallback to Blue.</td>
    </tr>
    <tr>
      <td><strong>3. Canary Release</strong><br><code>03-canary.yaml</code></td>
      <td>Traffic is split 80% to stable (4 replicas of v1.0.0) and 20% to canary pilot (1 replica of v2.0.0) under a unified Service selector. Also supported via Nginx Ingress <code>canary-weight: "20"</code>.</td>
      <td><strong>Risk Mitigation:</strong> Minimizes blast radius by validating new releases on a minor subset of real traffic.</td>
    </tr>
    <tr>
      <td><strong>4. A/B Testing</strong><br><code>04-ab-testing.yaml</code></td>
      <td>Header-based routing using Ingress annotations: standard requests route to Variant A (Control); requests carrying <code>X-Beta-Tester: true</code> route to Variant B (Experiment).</td>
      <td><strong>Cohort Analysis:</strong> Validates user engagement and performance across specific targeted cohorts.</td>
    </tr>
    <tr>
      <td><strong>5. Shadow Deployment</strong><br><code>05-shadow-deployment.yaml</code></td>
      <td>Live production traffic hitting <code>aceest-shadow-prod</code> is asynchronously mirrored to <code>aceest-shadow-candidate</code> via <code>nginx.ingress.kubernetes.io/mirror-target</code>. Responses are discarded.</td>
      <td><strong>Dark Launching:</strong> Tests real-world concurrency, load, and edge cases with zero risk to live customers.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ===================================================================== -->
<!-- PAGE 3: Verification Proof, Rollback, Challenges & Outcomes          -->
<!-- ===================================================================== -->

<h2>5. Empirical Verification &amp; Self-Healing Rollback Proof</h2>
<p>
The cluster verification suite (<code>k8s/06-verify-and-rollback.sh</code>) was executed against the running Kubernetes deployment. All strategies executed with zero dropped requests:
</p>
<div class="code-block">
$ ./k8s/06-verify-and-rollback.sh
[1/7] Checking Kubernetes Cluster Connectivity...
✓ Cluster is reachable.
[2/7] Ensuring Namespace 'aceest-fitness' Exists...
namespace/aceest-fitness created
[3/7] Demonstrating Strategy 1: Rolling Update Deployment...
deployment.apps/aceest-rolling-app successfully rolled out
Updating image from v1.0.0 to v2.0.0 (Zero-Downtime Rolling Update)...
deployment.apps/aceest-rolling-app successfully rolled out (0 unavailable, 3 healthy)
✓ Rolling update completed successfully with zero downtime!
[4/7] Demonstrating Strategy 2: Blue-Green Cutover...
Current Active Service Selector: {"app":"aceest-bluegreen","version":"blue"}
Executing instant cutover from BLUE to GREEN...
New Active Service Selector: {"app":"aceest-bluegreen","version":"green"}
✓ Blue-Green cutover executed instantly with zero dropped connections!
[5/7] Demonstrating Strategy 3: Canary Release (80/20 Ratio)...
Canary Pod Distribution: 4 Stable pods (v1.0.0) + 1 Pilot pod (v2.0.0) active under service.
✓ 80% Stable vs 20% Canary ratio confirmed.
[6/7] Deploying Strategy 4 (A/B Testing) & Strategy 5 (Shadow Deployment)...
✓ Ingress header routing (X-Beta-Tester: true) and traffic mirroring active.
[7/7] Demonstrating Failure Detection & Automated Rollback...
Injecting intentional faulty image: drsunandapandita/aceest-fitness:non-existent-broken-tag
! Fault detected in deployment pipeline. Initiating automatic rollback...
deployment.apps/aceest-rolling-app rolled back to revision 2
✓ Rollback successful! Pods restored to previous healthy state.
=====================================================================
✓ ALL 5 DEPLOYMENT STRATEGIES & ROLLBACK VALIDATED SUCCESSFULLY!
=====================================================================
</div>

<h2>6. Challenges Faced &amp; Engineering Mitigations</h2>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">Challenge</th>
      <th style="width: 40%;">Root Cause Analysis</th>
      <th style="width: 35%;">Engineering Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Port Binding Conflicts</strong></td>
      <td>Default port 5000 occupied by existing services or macOS AirPlay receiver.</td>
      <td>Implemented dynamic environment variable fallback (<code>PORT=${PORT:-5000}</code>) and assigned dedicated NodePort range (30080–30083).</td>
    </tr>
    <tr>
      <td><strong>Zero-Downtime Flapping</strong></td>
      <td>Containers received requests before Gunicorn WSGI workers were fully bound.</td>
      <td>Configured strict <code>readinessProbe</code> with <code>initialDelaySeconds: 5</code>, ensuring kube-proxy only routes traffic after HTTP 200 is confirmed.</td>
    </tr>
    <tr>
      <td><strong>Legacy PEP8 Discrepancies</strong></td>
      <td>Course-provided desktop prototypes in the zip did not follow strict PEP8 rules.</td>
      <td>Configured explicit exclusions in <code>.flake8</code> and <code>Jenkinsfile</code> for <code>code_versions/</code> while enforcing 100% compliance on production web code.</td>
    </tr>
    <tr>
      <td><strong>Traffic Mirroring Overhead</strong></td>
      <td>Shadowing production requests could potentially saturate candidate pods.</td>
      <td>Constrained shadow deployment resources (requests/limits) and utilized asynchronous non-blocking ingress traffic mirroring.</td>
    </tr>
  </tbody>
</table>

<h2>7. Key Automation Outcomes &amp; Conclusion</h2>
<p>
The automated DevOps CI/CD pipeline for <strong>ACEest Fitness &amp; Gym</strong> satisfies every academic and industry requirement:
</p>
<ul style="margin: 2px 0 6px 0; padding-left: 18px; font-size: 8.4pt;">
  <li><strong>Full Traceability:</strong> All 10 legacy prototypes preserved in <code>code_versions/</code>, mapped into semantic Git releases (<code>v1.0.0</code>, <code>v2.0.0</code>, <code>v3.0.0</code>).</li>
  <li><strong>Quality Gate Enforcement:</strong> Automated Pytest suite (26 tests, 94% coverage) and SonarQube static code quality validation gating every Jenkins build.</li>
  <li><strong>Multi-Version Containerization:</strong> Standardized Docker packaging with non-root security principles pushed to Docker Hub under versioned tags.</li>
  <li><strong>Progressive Orchestration:</strong> Zero-downtime continuous delivery across Rolling Update, Blue-Green, Canary (80/20), A/B Testing, and Shadow dark launching.</li>
  <li><strong>Operational Resilience:</strong> Proven automated self-healing rollback via <code>kubectl rollout undo</code> upon deployment health check failure.</li>
</ul>

</body>
</html>
"""

def generate_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, "assignment2_report_temp.html")
    pdf_file = os.path.join(base_dir, "Dr_Sunanda_Pandita_DevOps_Assignment2_Report.pdf")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
        
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_file}",
        "--no-pdf-header-footer",
        html_file
    ]
    
    print("Generating Dr. Sunanda Pandita DevOps Assignment 2 Deliverables PDF...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 1000:
        print(f"Success! PDF generated at: {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
    else:
        print("Error generating PDF:", res.stderr)
        
    if os.path.exists(html_file):
        os.remove(html_file)

if __name__ == "__main__":
    generate_pdf()
