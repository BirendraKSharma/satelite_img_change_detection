# 🔑 API Key Setup Guide

## Quick Setup (Recommended)

### Step 1: Get Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key (starts with `AIza...`)

### Step 2: Create .env File
1. Copy the example file:
   ```bash
   cp .env.example .env
   ```
   
   Or on Windows:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` file in a text editor

3. Replace `your_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=AIzaSyABC123def456GHI789jkl012MNO345pqr
   ```

4. Save the file

### Step 3: Run the Application
```bash
streamlit run app.py
```

The API key will be automatically loaded from the `.env` file! ✅

## Alternative: Manual Entry

If you prefer not to use a `.env` file:
1. Run the application: `streamlit run app.py`
2. Enter your API key in the sidebar
3. Check "Enable AI Summary"

## Security Best Practices

✅ **DO:**
- Store API keys in `.env` file (already in .gitignore)
- Keep `.env` file private
- Use `.env.example` for sharing setup instructions
- Rotate keys periodically

❌ **DON'T:**
- Commit `.env` file to git
- Share API keys publicly
- Hardcode keys in source code
- Use keys in screenshots

## Troubleshooting

### "API key not provided"
- Check that `.env` file exists in project root
- Verify the key is on the correct line: `GEMINI_API_KEY=your_key`
- No quotes around the key value
- No spaces before/after the `=`

### "404 models/gemini-1.5-flash is not found"
✅ **Fixed!** Now using `gemini-pro` model which is available in all API versions.

### ".env file not loading"
- Restart the Streamlit app after creating `.env`
- Check file is named exactly `.env` (not `.env.txt`)
- Ensure `.env` is in the same directory as `app.py`

## Verification

To verify your setup works:

```bash
python test_ai_summary.py
```

This will:
1. Test the quick insight (no API needed)
2. Test the AI summary (requires API key)
3. Show example outputs

## Free Tier Limits

Google AI Studio Free Tier:
- ✅ 60 requests per minute
- ✅ Free for development and testing
- ✅ No credit card required
- ✅ Sufficient for most use cases

## Need Help?

- [Google AI Studio Documentation](https://ai.google.dev/docs)
- [Get API Key](https://makersuite.google.com/app/apikey)
- [Pricing Info](https://ai.google.dev/pricing)

---

**Ready to use!** Your API key is now securely configured. 🔐✨
