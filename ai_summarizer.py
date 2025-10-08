"""
AI-powered summarization using Google Gemini API
Converts satellite change detection results into natural language
"""

import google.generativeai as genai
from typing import Dict, Optional


def generate_summary(stats: Dict, detection_method: str, api_key: Optional[str] = None) -> str:
    """
    Generate natural language summary of change detection results
    
    Args:
        stats: Dictionary containing change detection statistics
        detection_method: Name of the detection method used
        api_key: Google AI Studio API key
    
    Returns:
        Natural language summary string
    """
    if not api_key:
        return "⚠️ API key not provided. Please add your Google AI Studio API key in the sidebar."
    
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Create prompt
        prompt = f"""You are an expert satellite imagery analyst. Analyze the following change detection results and provide a clear, concise summary in 3-4 sentences for non-technical users.

Detection Method: {detection_method}
Total Pixels Analyzed: {stats.get('total_pixels', 0):,}
Changed Pixels: {stats.get('changed_pixels', 0):,}
Change Percentage: {stats.get('change_percentage', 0):.2f}%
Number of Change Regions: {stats.get('num_change_regions', 0)}
Average Region Size: {stats.get('avg_region_size', 0):.1f} pixels

Provide a professional summary that:
1. Describes the magnitude of change (minor, moderate, significant, dramatic)
2. Interprets what this might indicate (urban development, vegetation loss, natural changes, etc.)
3. Highlights key patterns or concerns
4. Keeps it simple and actionable for business intelligence purposes

Summary:"""
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        return f"⚠️ Error generating summary: {str(e)}\n\nPlease check your API key and internet connection."


def get_quick_insight(change_percentage: float) -> str:
    """
    Get quick insight without API call (fallback)
    
    Args:
        change_percentage: Percentage of changed area
    
    Returns:
        Simple insight string
    """
    if change_percentage < 5:
        return "✅ Minimal changes detected. Area appears relatively stable."
    elif change_percentage < 15:
        return "📊 Moderate changes observed. Worth investigating specific regions."
    elif change_percentage < 30:
        return "⚠️ Significant changes detected. Major transformations occurring."
    else:
        return "🚨 Dramatic changes identified. Substantial area modification detected."
