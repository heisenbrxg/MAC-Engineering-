import os

directory = r"e:\mac fin 2\mac fin 2\HTML_TEMPLATE"

replacements = {
    "Testimonials - Digital Marketing Agency": "Testimonials - MAC Engineering Services",
    "Single Services - Digital Marketing Agency": "Single Services - MAC Engineering Services",
    "Single Post - Digital Marketing Agency": "Single Post - MAC Engineering Services",
    "Search - Digital Marketing Agency": "Search - MAC Engineering Services",
    "Pricing Plan - Digital Marketing Agency": "Pricing Plan - MAC Engineering Services",
    "Partnership - Marko - Digital Marketing Agency": "Partnership - MAC Engineering Services",
    "Marko - Digital Marketing Agency": "MAC Engineering Services",
    "Digital Marketing Agency": "HVAC Solutions Provider",
    "Marko completely transformed our online presence! Their digital marketing strategies helped us double our revenue in just six months.": "MAC handled every aspect of our ventilation upgrade. Our indoor air quality improved significantly, and energy consumption dropped.",
    "From SEO to paid ads, Marko nailed every aspect of our campaign. Our website traffic skyrocketed, and lead generation has never been better!": "The turnaround time for emergency repairs was incredible. MAC ensures our systems run 24/7 without fail, and their AMC service is top-notch!",
    "We've worked with many agencies before, but Marko stands out. Their data-driven approach and creative solutions gave us an edge over competitors.": "We've worked with many contractors before, but MAC stands out. Their engineering approach and efficient solutions gave us complete peace of mind.",
    "Highly professional and results-oriented. Marko's expertise in branding and content marketing helped us build a strong online identity.": "Highly professional and results-oriented. MAC's expertise in HVAC design and cooling systems helped us build a reliable infrastructure.",
    "Discover how businesses like yours achieved outstanding growth with Marko's expert digital marketing solutions.": "Discover how businesses like yours achieved outstanding comfort and efficiency with MAC's expert HVAC engineering solutions.",
    "In the fast-paced digital world, choosing the right marketing partner makes all the difference. At Marko, we don’t just create campaigns—we craft strategies that deliver measurable success.": "In the world of high-efficiency climate control, choosing the right engineering partner is critical. At MAC, we don't just install machines—we design solutions that deliver lasting reliability.",
    "Partner with Marko & take your brand to the next level.": "Partner with MAC & optimize your infrastructure.",
    "Transform Your Business with Marko!": "Transform Your Infrastructure with MAC!",
    "Take your digital marketing to the next level with data-driven strategies and innovative solutions. Let's create something amazing together!": "Take your facility's climate control to the next level with factory-trained engineers. Let's create a perfect environment together!",
    "Why Choose Marko": "Why Choose MAC Engineering",
    "Marko's": "MAC's",
    "Marko": "MAC",
    "Digital Marketing": "HVAC Engineering",
    "digital marketing": "HVAC engineering",
    "digital growth": "HVAC installation",
    "marko-logo.png": "MAC logo.png",
    "marko-logo-dark.png": "MAC logo.png",
    "hello@markoagency.com": "info@maceng.in",
    "123 Digital Street, New York, USA": "35/1, Alwarthirunagar First Main Road, Chennai - 600 087",
    "2025 Marko. Fox Creation All Rights Reserved.": "2025 MAC Engineering Services. All Rights Reserved.",
    "Digital Success": "Optimal HVAC Performance",
    "Digital Business": "HVAC Infrastructure",
    "Digital Presence": "HVAC System",
    "Digital Solutions That Drive Real Results": "HVAC Solutions That Drive Real Comfort",
    "Digital Process": "HVAC Process",
    "digital process": "HVAC process"
}

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html") or file.endswith(".js") or file.endswith(".php"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old_str, new_str in replacements.items():
                new_content = new_content.replace(old_str, new_str)
                
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")

print("Done replacing.")
