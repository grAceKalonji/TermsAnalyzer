from analyzer import TermsAnalyzer

analyzer = TermsAnalyzer("google_terms_of_service_en_us.pdf")
summary = analyzer.summarize()

print(f"summary: {summary}")