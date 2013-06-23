"""
Cribbed from http://schema.rdfs.org/all.json
"""
def to_python(strval, schema_type):
    pass

schema = {
  "datatypes": {
    "Boolean": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "Boolean: True or False.", 
      "comment_plain": "Boolean: True or False.", 
      "id": "Boolean", 
      "instances": [
        "False", 
        "True"
      ], 
      "label": "Boolean", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/Boolean"
    }, 
    "DataType": {
      "ancestors": [], 
      "comment": "The basic data types such as Integers, Strings, etc.", 
      "comment_plain": "The basic data types such as Integers, Strings, etc.", 
      "id": "DataType", 
      "label": "Data Type", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [
        "Boolean", 
        "Date", 
        "DateTime", 
        "Number", 
        "Text", 
        "Time"
      ], 
      "supertypes": [], 
      "url": "http://schema.org/DataType"
    }, 
    "Date": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "A date value in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 date format</a>.", 
      "comment_plain": "A date value in ISO 8601 date format.", 
      "id": "Date", 
      "label": "Date", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/Date"
    }, 
    "DateTime": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).", 
      "comment_plain": "A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).", 
      "id": "DateTime", 
      "label": "Date Time", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/DateTime"
    }, 
    "Float": {
      "ancestors": [
        "DataType", 
        "Number"
      ], 
      "comment": "Data type: Floating number.", 
      "comment_plain": "Data type: Floating number.", 
      "id": "Float", 
      "label": "Float", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Number"
      ], 
      "url": "http://schema.org/Float"
    }, 
    "Integer": {
      "ancestors": [
        "DataType", 
        "Number"
      ], 
      "comment": "Data type: Integer.", 
      "comment_plain": "Data type: Integer.", 
      "id": "Integer", 
      "label": "Integer", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Number"
      ], 
      "url": "http://schema.org/Integer"
    }, 
    "Number": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "Data type: Number.", 
      "comment_plain": "Data type: Number.", 
      "id": "Number", 
      "label": "Number", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [
        "Float", 
        "Integer"
      ], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/Number"
    }, 
    "Text": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "Data type: Text.", 
      "comment_plain": "Data type: Text.", 
      "id": "Text", 
      "label": "Text", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [
        "URL"
      ], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/Text"
    }, 
    "Time": {
      "ancestors": [
        "DataType"
      ], 
      "comment": "A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see <a href=\"http://www.w3.org/TR/xmlschema-2/#time\">XML schema for details</a>).", 
      "comment_plain": "A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see XML schema for details).", 
      "id": "Time", 
      "label": "Time", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DataType"
      ], 
      "url": "http://schema.org/Time"
    }, 
    "URL": {
      "ancestors": [
        "DataType", 
        "Text"
      ], 
      "comment": "Data type: URL.", 
      "comment_plain": "Data type: URL.", 
      "id": "URL", 
      "label": "URL", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Text"
      ], 
      "url": "http://schema.org/URL"
    }
  }, 
  "properties": {
    "about": {
      "comment": "The subject matter of the content.", 
      "comment_plain": "The subject matter of the content.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "about", 
      "label": "About", 
      "ranges": [
        "Thing"
      ]
    }, 
    "acceptedPaymentMethod": {
      "comment": "The payment method(s) accepted by seller for this offer.", 
      "comment_plain": "The payment method(s) accepted by seller for this offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "acceptedPaymentMethod", 
      "label": "Accepted Payment Method", 
      "ranges": [
        "PaymentMethod"
      ]
    }, 
    "acceptsReservations": {
      "comment": "Either <code>Yes/No</code>, or a URL at which reservations can be made.", 
      "comment_plain": "Either Yes/No, or a URL at which reservations can be made.", 
      "domains": [
        "FoodEstablishment"
      ], 
      "id": "acceptsReservations", 
      "label": "Accepts Reservations", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "accountablePerson": {
      "comment": "Specifies the Person that is legally accountable for the CreativeWork.", 
      "comment_plain": "Specifies the Person that is legally accountable for the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "accountablePerson", 
      "label": "Accountable Person", 
      "ranges": [
        "Person"
      ]
    }, 
    "acquiredFrom": {
      "comment": "The organization or person from which the product was acquired.", 
      "comment_plain": "The organization or person from which the product was acquired.", 
      "domains": [
        "OwnershipInfo"
      ], 
      "id": "acquiredFrom", 
      "label": "Acquired From", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "action": {
      "comment": "The movement the muscle generates.", 
      "comment_plain": "The movement the muscle generates.", 
      "domains": [
        "Muscle"
      ], 
      "id": "action", 
      "label": "Action", 
      "ranges": [
        "Text"
      ]
    }, 
    "activeIngredient": {
      "comment": "An active ingredient, typically chemical compounds and/or biologic substances.", 
      "comment_plain": "An active ingredient, typically chemical compounds and/or biologic substances.", 
      "domains": [
        "DrugStrength", 
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "activeIngredient", 
      "label": "Active Ingredient", 
      "ranges": [
        "Text"
      ]
    }, 
    "activityDuration": {
      "comment": "Length of time to engage in the activity.", 
      "comment_plain": "Length of time to engage in the activity.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "activityDuration", 
      "label": "Activity Duration", 
      "ranges": [
        "Duration"
      ]
    }, 
    "activityFrequency": {
      "comment": "How often one should engage in the activity.", 
      "comment_plain": "How often one should engage in the activity.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "activityFrequency", 
      "label": "Activity Frequency", 
      "ranges": [
        "Text"
      ]
    }, 
    "actor": {
      "comment": "A cast member of the movie, TV series, season, or episode, or video.", 
      "comment_plain": "A cast member of the movie, TV series, season, or episode, or video.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries"
      ], 
      "id": "actor", 
      "label": "Actor", 
      "ranges": [
        "Person"
      ]
    }, 
    "actors": {
      "comment": "A cast member of the movie, TV series, season, or episode, or video. (legacy spelling; see singular form, actor)", 
      "comment_plain": "A cast member of the movie, TV series, season, or episode, or video. (legacy spelling; see singular form, actor)", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries"
      ], 
      "id": "actors", 
      "label": "Actors", 
      "ranges": [
        "Person"
      ]
    }, 
    "addOn": {
      "comment": "An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).", 
      "comment_plain": "An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).", 
      "domains": [
        "Offer"
      ], 
      "id": "addOn", 
      "label": "Add On", 
      "ranges": [
        "Offer"
      ]
    }, 
    "additionalName": {
      "comment": "An additional name for a Person, can be used for a middle name.", 
      "comment_plain": "An additional name for a Person, can be used for a middle name.", 
      "domains": [
        "Person"
      ], 
      "id": "additionalName", 
      "label": "Additional Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "additionalType": {
      "comment": "An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.", 
      "comment_plain": "An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.", 
      "domains": [
        "Thing"
      ], 
      "id": "additionalType", 
      "label": "Additional Type", 
      "ranges": [
        "URL"
      ]
    }, 
    "additionalVariable": {
      "comment": "Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.", 
      "comment_plain": "Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "additionalVariable", 
      "label": "Additional Variable", 
      "ranges": [
        "Text"
      ]
    }, 
    "address": {
      "comment": "Physical address of the item.", 
      "comment_plain": "Physical address of the item.", 
      "domains": [
        "Organization", 
        "Place", 
        "Person"
      ], 
      "id": "address", 
      "label": "Address", 
      "ranges": [
        "PostalAddress"
      ]
    }, 
    "addressCountry": {
      "comment": "The country. For example, USA. You can also provide the two-letter <a href=\"http://en.wikipedia.org/wiki/ISO_3166-1\">ISO 3166-1 alpha-2 country code</a>.", 
      "comment_plain": "The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "addressCountry", 
      "label": "Address Country", 
      "ranges": [
        "Country"
      ]
    }, 
    "addressLocality": {
      "comment": "The locality. For example, Mountain View.", 
      "comment_plain": "The locality. For example, Mountain View.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "addressLocality", 
      "label": "Address Locality", 
      "ranges": [
        "Text"
      ]
    }, 
    "addressRegion": {
      "comment": "The region. For example, CA.", 
      "comment_plain": "The region. For example, CA.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "addressRegion", 
      "label": "Address Region", 
      "ranges": [
        "Text"
      ]
    }, 
    "administrationRoute": {
      "comment": "A route by which this drug may be administered, e.g. 'oral'.", 
      "comment_plain": "A route by which this drug may be administered, e.g. 'oral'.", 
      "domains": [
        "Drug"
      ], 
      "id": "administrationRoute", 
      "label": "Administration Route", 
      "ranges": [
        "Text"
      ]
    }, 
    "advanceBookingRequirement": {
      "comment": "The amount of time that is required between accepting the offer and the actual usage of the resource or service.", 
      "comment_plain": "The amount of time that is required between accepting the offer and the actual usage of the resource or service.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "advanceBookingRequirement", 
      "label": "Advance Booking Requirement", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "adverseOutcome": {
      "comment": "A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.", 
      "comment_plain": "A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.", 
      "domains": [
        "MedicalDevice", 
        "MedicalTherapy"
      ], 
      "id": "adverseOutcome", 
      "label": "Adverse Outcome", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "affectedBy": {
      "comment": "Drugs that affect the test's results.", 
      "comment_plain": "Drugs that affect the test's results.", 
      "domains": [
        "MedicalTest"
      ], 
      "id": "affectedBy", 
      "label": "Affected by", 
      "ranges": [
        "Drug"
      ]
    }, 
    "affiliation": {
      "comment": "An organization that this person is affiliated with. For example, a school/university, a club, or a team.", 
      "comment_plain": "An organization that this person is affiliated with. For example, a school/university, a club, or a team.", 
      "domains": [
        "Person"
      ], 
      "id": "affiliation", 
      "label": "Affiliation", 
      "ranges": [
        "Organization"
      ]
    }, 
    "aggregateRating": {
      "comment": "The overall rating, based on a collection of reviews or ratings, of the item.", 
      "comment_plain": "The overall rating, based on a collection of reviews or ratings, of the item.", 
      "domains": [
        "Organization", 
        "Product", 
        "CreativeWork", 
        "Place", 
        "Offer"
      ], 
      "id": "aggregateRating", 
      "label": "Aggregate Rating", 
      "ranges": [
        "AggregateRating"
      ]
    }, 
    "album": {
      "comment": "A music album.", 
      "comment_plain": "A music album.", 
      "domains": [
        "MusicGroup"
      ], 
      "id": "album", 
      "label": "Album", 
      "ranges": [
        "MusicAlbum"
      ]
    }, 
    "albums": {
      "comment": "A collection of music albums (legacy spelling; see singular form, album).", 
      "comment_plain": "A collection of music albums (legacy spelling; see singular form, album).", 
      "domains": [
        "MusicGroup"
      ], 
      "id": "albums", 
      "label": "Albums", 
      "ranges": [
        "MusicAlbum"
      ]
    }, 
    "alcoholWarning": {
      "comment": "Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.", 
      "comment_plain": "Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.", 
      "domains": [
        "Drug"
      ], 
      "id": "alcoholWarning", 
      "label": "Alcohol Warning", 
      "ranges": [
        "Text"
      ]
    }, 
    "algorithm": {
      "comment": "The algorithm or rules to follow to compute the score.", 
      "comment_plain": "The algorithm or rules to follow to compute the score.", 
      "domains": [
        "MedicalRiskScore"
      ], 
      "id": "algorithm", 
      "label": "Algorithm", 
      "ranges": [
        "Text"
      ]
    }, 
    "alignmentType": {
      "comment": "A category of alignment between the learning resource and the framework node. Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.", 
      "comment_plain": "A category of alignment between the learning resource and the framework node. Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.", 
      "domains": [
        "AlignmentObject"
      ], 
      "id": "alignmentType", 
      "label": "Alignment Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "alternateName": {
      "comment": "Any alternate name for this medical entity.", 
      "comment_plain": "Any alternate name for this medical entity.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "alternateName", 
      "label": "Alternate Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "alternativeHeadline": {
      "comment": "A secondary title of the CreativeWork.", 
      "comment_plain": "A secondary title of the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "alternativeHeadline", 
      "label": "Alternative Headline", 
      "ranges": [
        "Text"
      ]
    }, 
    "alumni": {
      "comment": "Alumni of educational organization.", 
      "comment_plain": "Alumni of educational organization.", 
      "domains": [
        "EducationalOrganization"
      ], 
      "id": "alumni", 
      "label": "Alumni", 
      "ranges": [
        "Person"
      ]
    }, 
    "alumniOf": {
      "comment": "An educational organizations that the person is an alumni of.", 
      "comment_plain": "An educational organizations that the person is an alumni of.", 
      "domains": [
        "Person"
      ], 
      "id": "alumniOf", 
      "label": "Alumni of", 
      "ranges": [
        "EducationalOrganization"
      ]
    }, 
    "amountOfThisGood": {
      "comment": "The quantity of the goods included in the offer.", 
      "comment_plain": "The quantity of the goods included in the offer.", 
      "domains": [
        "TypeAndQuantityNode"
      ], 
      "id": "amountOfThisGood", 
      "label": "Amount of This Good", 
      "ranges": [
        "Number"
      ]
    }, 
    "antagonist": {
      "comment": "The muscle whose action counteracts the specified muscle.", 
      "comment_plain": "The muscle whose action counteracts the specified muscle.", 
      "domains": [
        "Muscle"
      ], 
      "id": "antagonist", 
      "label": "Antagonist", 
      "ranges": [
        "Muscle"
      ]
    }, 
    "applicableLocation": {
      "comment": "The location in which the status applies.", 
      "comment_plain": "The location in which the status applies.", 
      "domains": [
        "DrugLegalStatus", 
        "DrugCost"
      ], 
      "id": "applicableLocation", 
      "label": "Applicable Location", 
      "ranges": [
        "AdministrativeArea"
      ]
    }, 
    "applicationCategory": {
      "comment": "Type of software application, e.g. \"Game, Multimedia\".", 
      "comment_plain": "Type of software application, e.g. \"Game, Multimedia\".", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "applicationCategory", 
      "label": "Application Category", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "applicationSubCategory": {
      "comment": "Subcategory of the application, e.g. \"Arcade Game\".", 
      "comment_plain": "Subcategory of the application, e.g. \"Arcade Game\".", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "applicationSubCategory", 
      "label": "Application Sub Category", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "applicationSuite": {
      "comment": "The name of the application suite to which the application belongs (e.g. Excel belongs to Office)", 
      "comment_plain": "The name of the application suite to which the application belongs (e.g. Excel belongs to Office)", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "applicationSuite", 
      "label": "Application Suite", 
      "ranges": [
        "Text"
      ]
    }, 
    "appliesToDeliveryMethod": {
      "comment": "The delivery method(s) to which the delivery charge or payment charge specification applies.", 
      "comment_plain": "The delivery method(s) to which the delivery charge or payment charge specification applies.", 
      "domains": [
        "DeliveryChargeSpecification", 
        "PaymentChargeSpecification"
      ], 
      "id": "appliesToDeliveryMethod", 
      "label": "Applies to Delivery Method", 
      "ranges": [
        "DeliveryMethod"
      ]
    }, 
    "appliesToPaymentMethod": {
      "comment": "The payment method(s) to which the payment charge specification applies.", 
      "comment_plain": "The payment method(s) to which the payment charge specification applies.", 
      "domains": [
        "PaymentChargeSpecification"
      ], 
      "id": "appliesToPaymentMethod", 
      "label": "Applies to Payment Method", 
      "ranges": [
        "PaymentMethod"
      ]
    }, 
    "arterialBranch": {
      "comment": "The branches that comprise the arterial structure.", 
      "comment_plain": "The branches that comprise the arterial structure.", 
      "domains": [
        "Artery"
      ], 
      "id": "arterialBranch", 
      "label": "Arterial Branch", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "articleBody": {
      "comment": "The actual body of the article.", 
      "comment_plain": "The actual body of the article.", 
      "domains": [
        "Article"
      ], 
      "id": "articleBody", 
      "label": "Article Body", 
      "ranges": [
        "Text"
      ]
    }, 
    "articleSection": {
      "comment": "Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.", 
      "comment_plain": "Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.", 
      "domains": [
        "Article"
      ], 
      "id": "articleSection", 
      "label": "Article Section", 
      "ranges": [
        "Text"
      ]
    }, 
    "aspect": {
      "comment": "An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc.", 
      "comment_plain": "An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc.", 
      "domains": [
        "MedicalWebPage"
      ], 
      "id": "aspect", 
      "label": "Aspect", 
      "ranges": [
        "Text"
      ]
    }, 
    "assembly": {
      "comment": "Library file name e.g., mscorlib.dll, system.web.dll", 
      "comment_plain": "Library file name e.g., mscorlib.dll, system.web.dll", 
      "domains": [
        "APIReference"
      ], 
      "id": "assembly", 
      "label": "Assembly", 
      "ranges": [
        "Text"
      ]
    }, 
    "assemblyVersion": {
      "comment": "Associated product/technology version. e.g., .NET Framework 4.5", 
      "comment_plain": "Associated product/technology version. e.g., .NET Framework 4.5", 
      "domains": [
        "APIReference"
      ], 
      "id": "assemblyVersion", 
      "label": "Assembly Version", 
      "ranges": [
        "Text"
      ]
    }, 
    "associatedAnatomy": {
      "comment": "The anatomy of the underlying organ system or structures associated with this entity.", 
      "comment_plain": "The anatomy of the underlying organ system or structures associated with this entity.", 
      "domains": [
        "MedicalCondition", 
        "PhysicalActivity"
      ], 
      "id": "associatedAnatomy", 
      "label": "Associated Anatomy", 
      "ranges": [
        "AnatomicalSystem", 
        "SuperficialAnatomy", 
        "AnatomicalStructure"
      ]
    }, 
    "associatedArticle": {
      "comment": "A NewsArticle associated with the Media Object.", 
      "comment_plain": "A NewsArticle associated with the Media Object.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "associatedArticle", 
      "label": "Associated Article", 
      "ranges": [
        "NewsArticle"
      ]
    }, 
    "associatedMedia": {
      "comment": "The media objects that encode this creative work. This property is a synonym for encodings.", 
      "comment_plain": "The media objects that encode this creative work. This property is a synonym for encodings.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "associatedMedia", 
      "label": "Associated Media", 
      "ranges": [
        "MediaObject"
      ]
    }, 
    "associatedPathophysiology": {
      "comment": "If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.", 
      "comment_plain": "If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.", 
      "domains": [
        "SuperficialAnatomy", 
        "AnatomicalSystem", 
        "AnatomicalStructure"
      ], 
      "id": "associatedPathophysiology", 
      "label": "Associated Pathophysiology", 
      "ranges": [
        "Text"
      ]
    }, 
    "attendee": {
      "comment": "A person or organization attending the event.", 
      "comment_plain": "A person or organization attending the event.", 
      "domains": [
        "Event"
      ], 
      "id": "attendee", 
      "label": "Attendee", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "attendees": {
      "comment": "A person attending the event (legacy spelling; see singular form, attendee).", 
      "comment_plain": "A person attending the event (legacy spelling; see singular form, attendee).", 
      "domains": [
        "Event"
      ], 
      "id": "attendees", 
      "label": "Attendees", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "audience": {
      "comment": "The intended audience of the item, i.e. the group for whom the item was created.", 
      "comment_plain": "The intended audience of the item, i.e. the group for whom the item was created.", 
      "domains": [
        "Product", 
        "CreativeWork"
      ], 
      "id": "audience", 
      "label": "Audience", 
      "ranges": [
        "Audience"
      ]
    }, 
    "audio": {
      "comment": "An embedded audio object.", 
      "comment_plain": "An embedded audio object.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "audio", 
      "label": "Audio", 
      "ranges": [
        "AudioObject"
      ]
    }, 
    "author": {
      "comment": "The author of this content. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.", 
      "comment_plain": "The author of this content. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "author", 
      "label": "Author", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "availability": {
      "comment": "The availability of this item\u2014for example In stock, Out of stock, Pre-order, etc.", 
      "comment_plain": "The availability of this item\u2014for example In stock, Out of stock, Pre-order, etc.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "availability", 
      "label": "Availability", 
      "ranges": [
        "ItemAvailability"
      ]
    }, 
    "availabilityEnds": {
      "comment": "The end of the availability of the product or service included in the offer.", 
      "comment_plain": "The end of the availability of the product or service included in the offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "availabilityEnds", 
      "label": "Availability Ends", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "availabilityStarts": {
      "comment": "The beginning of the availability of the product or service included in the offer.", 
      "comment_plain": "The beginning of the availability of the product or service included in the offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "availabilityStarts", 
      "label": "Availability Starts", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "availableAtOrFrom": {
      "comment": "The place(s) from which the offer can be obtained (e.g. store locations).", 
      "comment_plain": "The place(s) from which the offer can be obtained (e.g. store locations).", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "availableAtOrFrom", 
      "label": "Available At or From", 
      "ranges": [
        "Place"
      ]
    }, 
    "availableDeliveryMethod": {
      "comment": "The delivery method(s) available for this offer.", 
      "comment_plain": "The delivery method(s) available for this offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "availableDeliveryMethod", 
      "label": "Available Delivery Method", 
      "ranges": [
        "DeliveryMethod"
      ]
    }, 
    "availableIn": {
      "comment": "The location in which the strength is available.", 
      "comment_plain": "The location in which the strength is available.", 
      "domains": [
        "DrugStrength"
      ], 
      "id": "availableIn", 
      "label": "Available in", 
      "ranges": [
        "AdministrativeArea"
      ]
    }, 
    "availableService": {
      "comment": "A medical service available from this provider.", 
      "comment_plain": "A medical service available from this provider.", 
      "domains": [
        "Physician", 
        "Hospital", 
        "MedicalClinic"
      ], 
      "id": "availableService", 
      "label": "Available Service", 
      "ranges": [
        "MedicalTest", 
        "MedicalProcedure", 
        "MedicalTherapy"
      ]
    }, 
    "availableStrength": {
      "comment": "An available dosage strength for the drug.", 
      "comment_plain": "An available dosage strength for the drug.", 
      "domains": [
        "Drug"
      ], 
      "id": "availableStrength", 
      "label": "Available Strength", 
      "ranges": [
        "DrugStrength"
      ]
    }, 
    "availableTest": {
      "comment": "A diagnostic test or procedure offered by this lab.", 
      "comment_plain": "A diagnostic test or procedure offered by this lab.", 
      "domains": [
        "DiagnosticLab"
      ], 
      "id": "availableTest", 
      "label": "Available Test", 
      "ranges": [
        "MedicalTest"
      ]
    }, 
    "award": {
      "comment": "An award won by this person or for this creative work.", 
      "comment_plain": "An award won by this person or for this creative work.", 
      "domains": [
        "Person", 
        "CreativeWork"
      ], 
      "id": "award", 
      "label": "Award", 
      "ranges": [
        "Text"
      ]
    }, 
    "awards": {
      "comment": "Awards won by this person or for this creative work. (legacy spelling; see singular form, award)", 
      "comment_plain": "Awards won by this person or for this creative work. (legacy spelling; see singular form, award)", 
      "domains": [
        "Person", 
        "CreativeWork"
      ], 
      "id": "awards", 
      "label": "Awards", 
      "ranges": [
        "Text"
      ]
    }, 
    "background": {
      "comment": "Descriptive information establishing a historical perspective on the supplement. May include the rationale for the name, the population where the supplement first came to prominence, etc.", 
      "comment_plain": "Descriptive information establishing a historical perspective on the supplement. May include the rationale for the name, the population where the supplement first came to prominence, etc.", 
      "domains": [
        "DietarySupplement"
      ], 
      "id": "background", 
      "label": "Background", 
      "ranges": [
        "Text"
      ]
    }, 
    "baseSalary": {
      "comment": "The base salary of the job.", 
      "comment_plain": "The base salary of the job.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "baseSalary", 
      "label": "Base Salary", 
      "ranges": [
        "Number"
      ]
    }, 
    "benefits": {
      "comment": "Description of benefits associated with the job.", 
      "comment_plain": "Description of benefits associated with the job.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "benefits", 
      "label": "Benefits", 
      "ranges": [
        "Text"
      ]
    }, 
    "bestRating": {
      "comment": "The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.", 
      "comment_plain": "The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.", 
      "domains": [
        "Rating"
      ], 
      "id": "bestRating", 
      "label": "Best Rating", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "billingIncrement": {
      "comment": "This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.", 
      "comment_plain": "This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.", 
      "domains": [
        "UnitPriceSpecification"
      ], 
      "id": "billingIncrement", 
      "label": "Billing Increment", 
      "ranges": [
        "Number"
      ]
    }, 
    "biomechnicalClass": {
      "comment": "The biomechanical properties of the bone.", 
      "comment_plain": "The biomechanical properties of the bone.", 
      "domains": [
        "Joint"
      ], 
      "id": "biomechnicalClass", 
      "label": "Biomechnical Class", 
      "ranges": [
        "Text"
      ]
    }, 
    "birthDate": {
      "comment": "Date of birth.", 
      "comment_plain": "Date of birth.", 
      "domains": [
        "Person"
      ], 
      "id": "birthDate", 
      "label": "Birth Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "bitrate": {
      "comment": "The bitrate of the media object.", 
      "comment_plain": "The bitrate of the media object.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "bitrate", 
      "label": "Bitrate", 
      "ranges": [
        "Text"
      ]
    }, 
    "blogPost": {
      "comment": "A posting that is part of this blog.", 
      "comment_plain": "A posting that is part of this blog.", 
      "domains": [
        "Blog"
      ], 
      "id": "blogPost", 
      "label": "Blog Post", 
      "ranges": [
        "BlogPosting"
      ]
    }, 
    "blogPosts": {
      "comment": "The postings that are part of this blog (legacy spelling; see singular form, blogPost).", 
      "comment_plain": "The postings that are part of this blog (legacy spelling; see singular form, blogPost).", 
      "domains": [
        "Blog"
      ], 
      "id": "blogPosts", 
      "label": "Blog Posts", 
      "ranges": [
        "BlogPosting"
      ]
    }, 
    "bloodSupply": {
      "comment": "The blood vessel that carries blood from the heart to the muscle.", 
      "comment_plain": "The blood vessel that carries blood from the heart to the muscle.", 
      "domains": [
        "Muscle"
      ], 
      "id": "bloodSupply", 
      "label": "Blood Supply", 
      "ranges": [
        "Vessel"
      ]
    }, 
    "bodyLocation": {
      "comment": "Location in the body of the anatomical structure.", 
      "comment_plain": "Location in the body of the anatomical structure.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "bodyLocation", 
      "label": "Body Location", 
      "ranges": [
        "Text"
      ]
    }, 
    "bookEdition": {
      "comment": "The edition of the book.", 
      "comment_plain": "The edition of the book.", 
      "domains": [
        "Book"
      ], 
      "id": "bookEdition", 
      "label": "Book Edition", 
      "ranges": [
        "Text"
      ]
    }, 
    "bookFormat": {
      "comment": "The format of the book.", 
      "comment_plain": "The format of the book.", 
      "domains": [
        "Book"
      ], 
      "id": "bookFormat", 
      "label": "Book Format", 
      "ranges": [
        "BookFormatType"
      ]
    }, 
    "box": {
      "comment": "A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more spacedelimited points where the first and final points are identical.", 
      "comment_plain": "A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more spacedelimited points where the first and final points are identical.", 
      "domains": [
        "GeoShape"
      ], 
      "id": "box", 
      "label": "Box", 
      "ranges": [
        "Text"
      ]
    }, 
    "branch": {
      "comment": "The branches that delineate from the nerve bundle.", 
      "comment_plain": "The branches that delineate from the nerve bundle.", 
      "domains": [
        "Nerve"
      ], 
      "id": "branch", 
      "label": "Branch", 
      "ranges": [
        "AnatomicalStructure", 
        "Nerve"
      ]
    }, 
    "branchOf": {
      "comment": "The larger organization that this local business is a branch of, if any.", 
      "comment_plain": "The larger organization that this local business is a branch of, if any.", 
      "domains": [
        "LocalBusiness"
      ], 
      "id": "branchOf", 
      "label": "Branch of", 
      "ranges": [
        "Organization"
      ]
    }, 
    "brand": {
      "comment": "The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.", 
      "comment_plain": "The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.", 
      "domains": [
        "Organization", 
        "Product", 
        "Person"
      ], 
      "id": "brand", 
      "label": "Brand", 
      "ranges": [
        "Organization", 
        "Brand"
      ]
    }, 
    "breadcrumb": {
      "comment": "A set of links that can help a user understand and navigate a website hierarchy.", 
      "comment_plain": "A set of links that can help a user understand and navigate a website hierarchy.", 
      "domains": [
        "WebPage"
      ], 
      "id": "breadcrumb", 
      "label": "Breadcrumb", 
      "ranges": [
        "Text"
      ]
    }, 
    "breastfeedingWarning": {
      "comment": "Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding mothers.", 
      "comment_plain": "Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding mothers.", 
      "domains": [
        "Drug"
      ], 
      "id": "breastfeedingWarning", 
      "label": "Breastfeeding Warning", 
      "ranges": [
        "Text"
      ]
    }, 
    "browserRequirements": {
      "comment": "Specifies browser requirements in human-readable text. For example,\"requires HTML5 support\".", 
      "comment_plain": "Specifies browser requirements in human-readable text. For example,\"requires HTML5 support\".", 
      "domains": [
        "WebApplication"
      ], 
      "id": "browserRequirements", 
      "label": "Browser Requirements", 
      "ranges": [
        "Text"
      ]
    }, 
    "businessFunction": {
      "comment": "The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.", 
      "comment_plain": "The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.", 
      "domains": [
        "Offer", 
        "TypeAndQuantityNode", 
        "Demand"
      ], 
      "id": "businessFunction", 
      "label": "Business Function", 
      "ranges": [
        "BusinessFunction"
      ]
    }, 
    "byArtist": {
      "comment": "The artist that performed this album or recording.", 
      "comment_plain": "The artist that performed this album or recording.", 
      "domains": [
        "MusicAlbum", 
        "MusicRecording"
      ], 
      "id": "byArtist", 
      "label": "By Artist", 
      "ranges": [
        "MusicGroup"
      ]
    }, 
    "calories": {
      "comment": "The number of calories", 
      "comment_plain": "The number of calories", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "calories", 
      "label": "Calories", 
      "ranges": [
        "Energy"
      ]
    }, 
    "caption": {
      "comment": "The caption for this object.", 
      "comment_plain": "The caption for this object.", 
      "domains": [
        "VideoObject", 
        "ImageObject"
      ], 
      "id": "caption", 
      "label": "Caption", 
      "ranges": [
        "Text"
      ]
    }, 
    "carbohydrateContent": {
      "comment": "The number of grams of carbohydrates.", 
      "comment_plain": "The number of grams of carbohydrates.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "carbohydrateContent", 
      "label": "Carbohydrate Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "carrierRequirements": {
      "comment": "Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).", 
      "comment_plain": "Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).", 
      "domains": [
        "MobileApplication"
      ], 
      "id": "carrierRequirements", 
      "label": "Carrier Requirements", 
      "ranges": [
        "Text"
      ]
    }, 
    "catalog": {
      "comment": "A data catalog which contains a dataset.", 
      "comment_plain": "A data catalog which contains a dataset.", 
      "domains": [
        "Dataset"
      ], 
      "id": "catalog", 
      "label": "Catalog", 
      "ranges": [
        "DataCatalog"
      ]
    }, 
    "category": {
      "comment": "A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.", 
      "comment_plain": "A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.", 
      "domains": [
        "PhysicalActivity", 
        "Offer"
      ], 
      "id": "category", 
      "label": "Category", 
      "ranges": [
        "Text", 
        "PhysicalActivityCategory", 
        "Thing"
      ]
    }, 
    "cause": {
      "comment": "An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.", 
      "comment_plain": "An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.", 
      "domains": [
        "MedicalCondition", 
        "MedicalSignOrSymptom"
      ], 
      "id": "cause", 
      "label": "Cause", 
      "ranges": [
        "MedicalCause"
      ]
    }, 
    "causeOf": {
      "comment": "The condition, complication, symptom, sign, etc. caused.", 
      "comment_plain": "The condition, complication, symptom, sign, etc. caused.", 
      "domains": [
        "MedicalCause"
      ], 
      "id": "causeOf", 
      "label": "Cause of", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "childMaxAge": {
      "comment": "Maximal age of the child", 
      "comment_plain": "Maximal age of the child", 
      "domains": [
        "ParentAudience"
      ], 
      "id": "childMaxAge", 
      "label": "Child Max Age", 
      "ranges": [
        "Number"
      ]
    }, 
    "childMinAge": {
      "comment": "Minimal age of the child", 
      "comment_plain": "Minimal age of the child", 
      "domains": [
        "ParentAudience"
      ], 
      "id": "childMinAge", 
      "label": "Child Min Age", 
      "ranges": [
        "Number"
      ]
    }, 
    "children": {
      "comment": "A child of the person.", 
      "comment_plain": "A child of the person.", 
      "domains": [
        "Person"
      ], 
      "id": "children", 
      "label": "Children", 
      "ranges": [
        "Person"
      ]
    }, 
    "cholesterolContent": {
      "comment": "The number of milligrams of cholesterol.", 
      "comment_plain": "The number of milligrams of cholesterol.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "cholesterolContent", 
      "label": "Cholesterol Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "circle": {
      "comment": "A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.", 
      "comment_plain": "A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.", 
      "domains": [
        "GeoShape"
      ], 
      "id": "circle", 
      "label": "Circle", 
      "ranges": [
        "Text"
      ]
    }, 
    "citation": {
      "comment": "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc. NOTE: Candidate for promotion to ScholarlyArticle.", 
      "comment_plain": "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc. NOTE: Candidate for promotion to ScholarlyArticle.", 
      "domains": [
        "MedicalScholarlyArticle"
      ], 
      "id": "citation", 
      "label": "Citation", 
      "ranges": [
        "CreativeWork", 
        "Text"
      ]
    }, 
    "clincalPharmacology": {
      "comment": "Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).", 
      "comment_plain": "Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).", 
      "domains": [
        "Drug"
      ], 
      "id": "clincalPharmacology", 
      "label": "Clincal Pharmacology", 
      "ranges": [
        "Text"
      ]
    }, 
    "closes": {
      "comment": "The closing hour of the place or service on the given day(s) of the week.", 
      "comment_plain": "The closing hour of the place or service on the given day(s) of the week.", 
      "domains": [
        "OpeningHoursSpecification"
      ], 
      "id": "closes", 
      "label": "Closes", 
      "ranges": [
        "Time"
      ]
    }, 
    "code": {
      "comment": "A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.", 
      "comment_plain": "A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "code", 
      "label": "Code", 
      "ranges": [
        "MedicalCode"
      ]
    }, 
    "codeRepository": {
      "comment": "Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex)", 
      "comment_plain": "Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex)", 
      "domains": [
        "Code"
      ], 
      "id": "codeRepository", 
      "label": "Code Repository", 
      "ranges": [
        "URL"
      ]
    }, 
    "codeValue": {
      "comment": "The actual code.", 
      "comment_plain": "The actual code.", 
      "domains": [
        "MedicalCode"
      ], 
      "id": "codeValue", 
      "label": "Code Value", 
      "ranges": [
        "Text"
      ]
    }, 
    "codingSystem": {
      "comment": "The coding system, e.g. 'ICD-10'.", 
      "comment_plain": "The coding system, e.g. 'ICD-10'.", 
      "domains": [
        "MedicalCode"
      ], 
      "id": "codingSystem", 
      "label": "Coding System", 
      "ranges": [
        "Text"
      ]
    }, 
    "colleague": {
      "comment": "A colleague of the person.", 
      "comment_plain": "A colleague of the person.", 
      "domains": [
        "Person"
      ], 
      "id": "colleague", 
      "label": "Colleague", 
      "ranges": [
        "Person"
      ]
    }, 
    "colleagues": {
      "comment": "A colleague of the person (legacy spelling; see singular form, colleague).", 
      "comment_plain": "A colleague of the person (legacy spelling; see singular form, colleague).", 
      "domains": [
        "Person"
      ], 
      "id": "colleagues", 
      "label": "Colleagues", 
      "ranges": [
        "Person"
      ]
    }, 
    "color": {
      "comment": "The color of the product.", 
      "comment_plain": "The color of the product.", 
      "domains": [
        "Product"
      ], 
      "id": "color", 
      "label": "Color", 
      "ranges": [
        "Text"
      ]
    }, 
    "comment": {
      "comment": "Comments, typically from users, on this CreativeWork.", 
      "comment_plain": "Comments, typically from users, on this CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "comment", 
      "label": "Comment", 
      "ranges": [
        "UserComments"
      ]
    }, 
    "commentText": {
      "comment": "The text of the UserComment.", 
      "comment_plain": "The text of the UserComment.", 
      "domains": [
        "UserComments"
      ], 
      "id": "commentText", 
      "label": "Comment Text", 
      "ranges": [
        "Text"
      ]
    }, 
    "commentTime": {
      "comment": "The time at which the UserComment was made.", 
      "comment_plain": "The time at which the UserComment was made.", 
      "domains": [
        "UserComments"
      ], 
      "id": "commentTime", 
      "label": "Comment Time", 
      "ranges": [
        "Date"
      ]
    }, 
    "comprisedOf": {
      "comment": "The underlying anatomical structures, such as organs, that comprise the anatomical system.", 
      "comment_plain": "The underlying anatomical structures, such as organs, that comprise the anatomical system.", 
      "domains": [
        "AnatomicalSystem"
      ], 
      "id": "comprisedOf", 
      "label": "Comprised of", 
      "ranges": [
        "AnatomicalStructure", 
        "AnatomicalSystem"
      ]
    }, 
    "connectedTo": {
      "comment": "Other anatomical structures to which this structure is connected.", 
      "comment_plain": "Other anatomical structures to which this structure is connected.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "connectedTo", 
      "label": "Connected to", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "contactPoint": {
      "comment": "A contact point for a person or organization.", 
      "comment_plain": "A contact point for a person or organization.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "contactPoint", 
      "label": "Contact Point", 
      "ranges": [
        "ContactPoint"
      ]
    }, 
    "contactPoints": {
      "comment": "A contact point for a person or organization (legacy spelling; see singular form, contactPoint).", 
      "comment_plain": "A contact point for a person or organization (legacy spelling; see singular form, contactPoint).", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "contactPoints", 
      "label": "Contact Points", 
      "ranges": [
        "ContactPoint"
      ]
    }, 
    "contactType": {
      "comment": "A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.", 
      "comment_plain": "A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.", 
      "domains": [
        "ContactPoint"
      ], 
      "id": "contactType", 
      "label": "Contact Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "containedIn": {
      "comment": "The basic containment relation between places.", 
      "comment_plain": "The basic containment relation between places.", 
      "domains": [
        "Place"
      ], 
      "id": "containedIn", 
      "label": "Contained in", 
      "ranges": [
        "Place"
      ]
    }, 
    "contentLocation": {
      "comment": "The location of the content.", 
      "comment_plain": "The location of the content.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "contentLocation", 
      "label": "Content Location", 
      "ranges": [
        "Place"
      ]
    }, 
    "contentRating": {
      "comment": "Official rating of a piece of content\u2014for example,'MPAA PG-13'.", 
      "comment_plain": "Official rating of a piece of content\u2014for example,'MPAA PG-13'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "contentRating", 
      "label": "Content Rating", 
      "ranges": [
        "Text"
      ]
    }, 
    "contentSize": {
      "comment": "File size in (mega/kilo) bytes.", 
      "comment_plain": "File size in (mega/kilo) bytes.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "contentSize", 
      "label": "Content Size", 
      "ranges": [
        "Text"
      ]
    }, 
    "contentUrl": {
      "comment": "Actual bytes of the media object, for example the image file or video file. (previous spelling: contentURL)", 
      "comment_plain": "Actual bytes of the media object, for example the image file or video file. (previous spelling: contentURL)", 
      "domains": [
        "MediaObject"
      ], 
      "id": "contentUrl", 
      "label": "Content Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "contraindication": {
      "comment": "A contraindication for this therapy.", 
      "comment_plain": "A contraindication for this therapy.", 
      "domains": [
        "MedicalDevice", 
        "MedicalTherapy"
      ], 
      "id": "contraindication", 
      "label": "Contraindication", 
      "ranges": [
        "MedicalContraindication"
      ]
    }, 
    "contributor": {
      "comment": "A secondary contributor to the CreativeWork.", 
      "comment_plain": "A secondary contributor to the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "contributor", 
      "label": "Contributor", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "cookTime": {
      "comment": "The time it takes to actually cook the dish, in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 duration format</a>.", 
      "comment_plain": "The time it takes to actually cook the dish, in ISO 8601 duration format.", 
      "domains": [
        "Recipe"
      ], 
      "id": "cookTime", 
      "label": "Cook Time", 
      "ranges": [
        "Duration"
      ]
    }, 
    "cookingMethod": {
      "comment": "The method of cooking, such as Frying, Steaming, ...", 
      "comment_plain": "The method of cooking, such as Frying, Steaming, ...", 
      "domains": [
        "Recipe"
      ], 
      "id": "cookingMethod", 
      "label": "Cooking Method", 
      "ranges": [
        "Text"
      ]
    }, 
    "copyrightHolder": {
      "comment": "The party holding the legal copyright to the CreativeWork.", 
      "comment_plain": "The party holding the legal copyright to the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "copyrightHolder", 
      "label": "Copyright Holder", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "copyrightYear": {
      "comment": "The year during which the claimed copyright for the CreativeWork was first asserted.", 
      "comment_plain": "The year during which the claimed copyright for the CreativeWork was first asserted.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "copyrightYear", 
      "label": "Copyright Year", 
      "ranges": [
        "Number"
      ]
    }, 
    "cost": {
      "comment": "Cost per unit of the drug, as reported by the source being tagged.", 
      "comment_plain": "Cost per unit of the drug, as reported by the source being tagged.", 
      "domains": [
        "Drug"
      ], 
      "id": "cost", 
      "label": "Cost", 
      "ranges": [
        "DrugCost"
      ]
    }, 
    "costCategory": {
      "comment": "The category of cost, such as wholesale, retail, reimbursement cap, etc.", 
      "comment_plain": "The category of cost, such as wholesale, retail, reimbursement cap, etc.", 
      "domains": [
        "DrugCost"
      ], 
      "id": "costCategory", 
      "label": "Cost Category", 
      "ranges": [
        "DrugCostCategory"
      ]
    }, 
    "costCurrency": {
      "comment": "The currency (in 3-letter <a href=\"http://en.wikipedia.org/wiki/ISO_4217\">ISO 4217 format</a>) of the drug cost.", 
      "comment_plain": "The currency (in 3-letter ISO 4217 format) of the drug cost.", 
      "domains": [
        "DrugCost"
      ], 
      "id": "costCurrency", 
      "label": "Cost Currency", 
      "ranges": [
        "Text"
      ]
    }, 
    "costOrigin": {
      "comment": "Additional details to capture the origin of the cost data. For example, 'Medicare Part B'.", 
      "comment_plain": "Additional details to capture the origin of the cost data. For example, 'Medicare Part B'.", 
      "domains": [
        "DrugCost"
      ], 
      "id": "costOrigin", 
      "label": "Cost Origin", 
      "ranges": [
        "Text"
      ]
    }, 
    "costPerUnit": {
      "comment": "The cost per unit of the drug.", 
      "comment_plain": "The cost per unit of the drug.", 
      "domains": [
        "DrugCost"
      ], 
      "id": "costPerUnit", 
      "label": "Cost Per Unit", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "countriesNotSupported": {
      "comment": "Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.", 
      "comment_plain": "Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "countriesNotSupported", 
      "label": "Countries Not Supported", 
      "ranges": [
        "Text"
      ]
    }, 
    "countriesSupported": {
      "comment": "Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.", 
      "comment_plain": "Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "countriesSupported", 
      "label": "Countries Supported", 
      "ranges": [
        "Text"
      ]
    }, 
    "creator": {
      "comment": "The creator/author of this CreativeWork or UserComments. This is the same as the Author property for CreativeWork.", 
      "comment_plain": "The creator/author of this CreativeWork or UserComments. This is the same as the Author property for CreativeWork.", 
      "domains": [
        "UserComments", 
        "CreativeWork"
      ], 
      "id": "creator", 
      "label": "Creator", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "currenciesAccepted": {
      "comment": "The currency accepted (in <a href=\"http://en.wikipedia.org/wiki/ISO_4217\">ISO 4217 currency format</a>).", 
      "comment_plain": "The currency accepted (in ISO 4217 currency format).", 
      "domains": [
        "LocalBusiness"
      ], 
      "id": "currenciesAccepted", 
      "label": "Currencies Accepted", 
      "ranges": [
        "Text"
      ]
    }, 
    "dataset": {
      "comment": "A dataset contained in a catalog.", 
      "comment_plain": "A dataset contained in a catalog.", 
      "domains": [
        "DataCatalog"
      ], 
      "id": "dataset", 
      "label": "Dataset", 
      "ranges": [
        "Dataset"
      ]
    }, 
    "dateCreated": {
      "comment": "The date on which the CreativeWork was created.", 
      "comment_plain": "The date on which the CreativeWork was created.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "dateCreated", 
      "label": "Date Created", 
      "ranges": [
        "Date"
      ]
    }, 
    "dateModified": {
      "comment": "The date on which the CreativeWork was most recently modified.", 
      "comment_plain": "The date on which the CreativeWork was most recently modified.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "dateModified", 
      "label": "Date Modified", 
      "ranges": [
        "Date"
      ]
    }, 
    "datePosted": {
      "comment": "Publication date for the job posting.", 
      "comment_plain": "Publication date for the job posting.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "datePosted", 
      "label": "Date Posted", 
      "ranges": [
        "Date"
      ]
    }, 
    "datePublished": {
      "comment": "Date of first broadcast/publication.", 
      "comment_plain": "Date of first broadcast/publication.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "datePublished", 
      "label": "Date Published", 
      "ranges": [
        "Date"
      ]
    }, 
    "dateline": {
      "comment": "The location where the NewsArticle was produced.", 
      "comment_plain": "The location where the NewsArticle was produced.", 
      "domains": [
        "NewsArticle"
      ], 
      "id": "dateline", 
      "label": "Dateline", 
      "ranges": [
        "Text"
      ]
    }, 
    "dayOfWeek": {
      "comment": "The day of the week for which these opening hours are valid.", 
      "comment_plain": "The day of the week for which these opening hours are valid.", 
      "domains": [
        "OpeningHoursSpecification"
      ], 
      "id": "dayOfWeek", 
      "label": "Day of Week", 
      "ranges": [
        "DayOfWeek"
      ]
    }, 
    "deathDate": {
      "comment": "Date of death.", 
      "comment_plain": "Date of death.", 
      "domains": [
        "Person"
      ], 
      "id": "deathDate", 
      "label": "Death Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "deliveryLeadTime": {
      "comment": "The typical delay between the receipt of the order and the goods leaving the warehouse.", 
      "comment_plain": "The typical delay between the receipt of the order and the goods leaving the warehouse.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "deliveryLeadTime", 
      "label": "Delivery Lead Time", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "dependencies": {
      "comment": "Prerequisites needed to fulfill steps in article.", 
      "comment_plain": "Prerequisites needed to fulfill steps in article.", 
      "domains": [
        "TechArticle"
      ], 
      "id": "dependencies", 
      "label": "Dependencies", 
      "ranges": [
        "Text"
      ]
    }, 
    "depth": {
      "comment": "The depth of the product.", 
      "comment_plain": "The depth of the product.", 
      "domains": [
        "Product"
      ], 
      "id": "depth", 
      "label": "Depth", 
      "ranges": [
        "Distance", 
        "QuantitativeValue"
      ]
    }, 
    "description": {
      "comment": "A short description of the item.", 
      "comment_plain": "A short description of the item.", 
      "domains": [
        "Thing"
      ], 
      "id": "description", 
      "label": "Description", 
      "ranges": [
        "Text"
      ]
    }, 
    "device": {
      "comment": "Device required to run the application. Used in cases where a specific make/model is required to run the application.", 
      "comment_plain": "Device required to run the application. Used in cases where a specific make/model is required to run the application.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "device", 
      "label": "Device", 
      "ranges": [
        "Text"
      ]
    }, 
    "diagnosis": {
      "comment": "One or more alternative conditions considered in the differential diagnosis process.", 
      "comment_plain": "One or more alternative conditions considered in the differential diagnosis process.", 
      "domains": [
        "DDxElement"
      ], 
      "id": "diagnosis", 
      "label": "Diagnosis", 
      "ranges": [
        "MedicalCondition"
      ]
    }, 
    "diagram": {
      "comment": "An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.", 
      "comment_plain": "An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "diagram", 
      "label": "Diagram", 
      "ranges": [
        "ImageObject"
      ]
    }, 
    "dietFeatures": {
      "comment": "Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body's approved dietary guidelines.", 
      "comment_plain": "Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body's approved dietary guidelines.", 
      "domains": [
        "Diet"
      ], 
      "id": "dietFeatures", 
      "label": "Diet Features", 
      "ranges": [
        "Text"
      ]
    }, 
    "differentialDiagnosis": {
      "comment": "One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.", 
      "comment_plain": "One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "differentialDiagnosis", 
      "label": "Differential Diagnosis", 
      "ranges": [
        "DDxElement"
      ]
    }, 
    "director": {
      "comment": "The director of the movie, TV episode, or series.", 
      "comment_plain": "The director of the movie, TV episode, or series.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries"
      ], 
      "id": "director", 
      "label": "Director", 
      "ranges": [
        "Person"
      ]
    }, 
    "discusses": {
      "comment": "Specifies the CreativeWork associated with the UserComment.", 
      "comment_plain": "Specifies the CreativeWork associated with the UserComment.", 
      "domains": [
        "UserComments"
      ], 
      "id": "discusses", 
      "label": "Discusses", 
      "ranges": [
        "CreativeWork"
      ]
    }, 
    "discussionUrl": {
      "comment": "A link to the page containing the comments of the CreativeWork.", 
      "comment_plain": "A link to the page containing the comments of the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "discussionUrl", 
      "label": "Discussion Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "distinguishingSign": {
      "comment": "One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.", 
      "comment_plain": "One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.", 
      "domains": [
        "DDxElement"
      ], 
      "id": "distinguishingSign", 
      "label": "Distinguishing Sign", 
      "ranges": [
        "MedicalSignOrSymptom"
      ]
    }, 
    "distribution": {
      "comment": "A downloadable form of this dataset, at a specific location, in a specific format.", 
      "comment_plain": "A downloadable form of this dataset, at a specific location, in a specific format.", 
      "domains": [
        "Dataset"
      ], 
      "id": "distribution", 
      "label": "Distribution", 
      "ranges": [
        "DataDownload"
      ]
    }, 
    "domainIncludes": {
      "comment": "Relates a property to a class that is (one of) the type(s) the property is expected to be used on.", 
      "comment_plain": "Relates a property to a class that is (one of) the type(s) the property is expected to be used on.", 
      "domains": [
        "Property"
      ], 
      "id": "domainIncludes", 
      "label": "Domain Includes", 
      "ranges": [
        "Class"
      ]
    }, 
    "dosageForm": {
      "comment": "A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'.", 
      "comment_plain": "A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'.", 
      "domains": [
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "dosageForm", 
      "label": "Dosage Form", 
      "ranges": [
        "Text"
      ]
    }, 
    "doseSchedule": {
      "comment": "A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.", 
      "comment_plain": "A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.", 
      "domains": [
        "Drug"
      ], 
      "id": "doseSchedule", 
      "label": "Dose Schedule", 
      "ranges": [
        "DoseSchedule"
      ]
    }, 
    "doseUnit": {
      "comment": "The unit of the dose, e.g. 'mg'.", 
      "comment_plain": "The unit of the dose, e.g. 'mg'.", 
      "domains": [
        "DoseSchedule"
      ], 
      "id": "doseUnit", 
      "label": "Dose Unit", 
      "ranges": [
        "Text"
      ]
    }, 
    "doseValue": {
      "comment": "The value of the dose, e.g. 500.", 
      "comment_plain": "The value of the dose, e.g. 500.", 
      "domains": [
        "DoseSchedule"
      ], 
      "id": "doseValue", 
      "label": "Dose Value", 
      "ranges": [
        "Number"
      ]
    }, 
    "downloadUrl": {
      "comment": "If the file can be downloaded, URL to download the binary.", 
      "comment_plain": "If the file can be downloaded, URL to download the binary.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "downloadUrl", 
      "label": "Download Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "drainsTo": {
      "comment": "The vasculature that the vein drains into.", 
      "comment_plain": "The vasculature that the vein drains into.", 
      "domains": [
        "Vein"
      ], 
      "id": "drainsTo", 
      "label": "Drains to", 
      "ranges": [
        "Vessel"
      ]
    }, 
    "drug": {
      "comment": "A drug in this drug class.", 
      "comment_plain": "A drug in this drug class.", 
      "domains": [
        "DrugClass"
      ], 
      "id": "drug", 
      "label": "Drug", 
      "ranges": [
        "Drug"
      ]
    }, 
    "drugClass": {
      "comment": "The class of drug this belongs to (e.g., statins).", 
      "comment_plain": "The class of drug this belongs to (e.g., statins).", 
      "domains": [
        "Drug"
      ], 
      "id": "drugClass", 
      "label": "Drug Class", 
      "ranges": [
        "DrugClass"
      ]
    }, 
    "drugUnit": {
      "comment": "The unit in which the drug is measured, e.g. '5 mg tablet'.", 
      "comment_plain": "The unit in which the drug is measured, e.g. '5 mg tablet'.", 
      "domains": [
        "DrugCost"
      ], 
      "id": "drugUnit", 
      "label": "Drug Unit", 
      "ranges": [
        "Text"
      ]
    }, 
    "duns": {
      "comment": "The Dun & Bradstreet DUNS number for identifying an organization or business person.", 
      "comment_plain": "The Dun & Bradstreet DUNS number for identifying an organization or business person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "duns", 
      "label": "Duns", 
      "ranges": [
        "Text"
      ]
    }, 
    "duplicateTherapy": {
      "comment": "A therapy that duplicates or overlaps this one.", 
      "comment_plain": "A therapy that duplicates or overlaps this one.", 
      "domains": [
        "MedicalTherapy"
      ], 
      "id": "duplicateTherapy", 
      "label": "Duplicate Therapy", 
      "ranges": [
        "MedicalTherapy"
      ]
    }, 
    "duration": {
      "comment": "The duration of the item (movie, audio recording, event, etc.) in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 date format</a>.", 
      "comment_plain": "The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.", 
      "domains": [
        "Movie", 
        "MediaObject", 
        "MusicRecording", 
        "Event"
      ], 
      "id": "duration", 
      "label": "Duration", 
      "ranges": [
        "Duration"
      ]
    }, 
    "durationOfWarranty": {
      "comment": "The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.", 
      "comment_plain": "The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.", 
      "domains": [
        "WarrantyPromise"
      ], 
      "id": "durationOfWarranty", 
      "label": "Duration of Warranty", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "editor": {
      "comment": "Specifies the Person who edited the CreativeWork.", 
      "comment_plain": "Specifies the Person who edited the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "editor", 
      "label": "Editor", 
      "ranges": [
        "Person"
      ]
    }, 
    "educationRequirements": {
      "comment": "Educational background needed for the position.", 
      "comment_plain": "Educational background needed for the position.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "educationRequirements", 
      "label": "Education Requirements", 
      "ranges": [
        "Text"
      ]
    }, 
    "educationalAlignment": {
      "comment": "An alignment to an established educational framework.", 
      "comment_plain": "An alignment to an established educational framework.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "educationalAlignment", 
      "label": "Educational Alignment", 
      "ranges": [
        "AlignmentObject"
      ]
    }, 
    "educationalFramework": {
      "comment": "The framework to which the resource being described is aligned.", 
      "comment_plain": "The framework to which the resource being described is aligned.", 
      "domains": [
        "AlignmentObject"
      ], 
      "id": "educationalFramework", 
      "label": "Educational Framework", 
      "ranges": [
        "Text"
      ]
    }, 
    "educationalRole": {
      "comment": "An educationalRole of an EducationalAudience", 
      "comment_plain": "An educationalRole of an EducationalAudience", 
      "domains": [
        "EducationalAudience"
      ], 
      "id": "educationalRole", 
      "label": "Educational Role", 
      "ranges": [
        "Text"
      ]
    }, 
    "educationalUse": {
      "comment": "The purpose of a work in the context of education; for example, 'assignment', 'group work'.", 
      "comment_plain": "The purpose of a work in the context of education; for example, 'assignment', 'group work'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "educationalUse", 
      "label": "Educational Use", 
      "ranges": [
        "Text"
      ]
    }, 
    "elevation": {
      "comment": "The elevation of a location.", 
      "comment_plain": "The elevation of a location.", 
      "domains": [
        "GeoShape", 
        "GeoCoordinates"
      ], 
      "id": "elevation", 
      "label": "Elevation", 
      "ranges": [
        "Text", 
        "Number"
      ]
    }, 
    "eligibleCustomerType": {
      "comment": "The type(s) of customers for which the given offer is valid.", 
      "comment_plain": "The type(s) of customers for which the given offer is valid.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "eligibleCustomerType", 
      "label": "Eligible Customer Type", 
      "ranges": [
        "BusinessEntityType"
      ]
    }, 
    "eligibleDuration": {
      "comment": "The duration for which the given offer is valid.", 
      "comment_plain": "The duration for which the given offer is valid.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "eligibleDuration", 
      "label": "Eligible Duration", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "eligibleQuantity": {
      "comment": "The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.", 
      "comment_plain": "The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.", 
      "domains": [
        "Demand", 
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "eligibleQuantity", 
      "label": "Eligible Quantity", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "eligibleRegion": {
      "comment": "The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.", 
      "comment_plain": "The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.", 
      "domains": [
        "DeliveryChargeSpecification", 
        "Offer", 
        "Demand"
      ], 
      "id": "eligibleRegion", 
      "label": "Eligible Region", 
      "ranges": [
        "Text", 
        "GeoShape"
      ]
    }, 
    "eligibleTransactionVolume": {
      "comment": "The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.", 
      "comment_plain": "The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.", 
      "domains": [
        "Demand", 
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "eligibleTransactionVolume", 
      "label": "Eligible Transaction Volume", 
      "ranges": [
        "PriceSpecification"
      ]
    }, 
    "email": {
      "comment": "Email address.", 
      "comment_plain": "Email address.", 
      "domains": [
        "Organization", 
        "ContactPoint", 
        "Person"
      ], 
      "id": "email", 
      "label": "Email", 
      "ranges": [
        "Text"
      ]
    }, 
    "embedUrl": {
      "comment": "A URL pointing to a player for a specific video. In general, this is the information in the <code>src</code> element of an <code>embed</code> tag and should not be the same as the content of the <code>loc</code> tag. (previous spelling: embedURL)", 
      "comment_plain": "A URL pointing to a player for a specific video. In general, this is the information in the src element of an embed tag and should not be the same as the content of the loc tag. (previous spelling: embedURL)", 
      "domains": [
        "MediaObject"
      ], 
      "id": "embedUrl", 
      "label": "Embed Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "employee": {
      "comment": "Someone working for this organization.", 
      "comment_plain": "Someone working for this organization.", 
      "domains": [
        "Organization"
      ], 
      "id": "employee", 
      "label": "Employee", 
      "ranges": [
        "Person"
      ]
    }, 
    "employees": {
      "comment": "People working for this organization. (legacy spelling; see singular form, employee)", 
      "comment_plain": "People working for this organization. (legacy spelling; see singular form, employee)", 
      "domains": [
        "Organization"
      ], 
      "id": "employees", 
      "label": "Employees", 
      "ranges": [
        "Person"
      ]
    }, 
    "employmentType": {
      "comment": "Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).", 
      "comment_plain": "Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).", 
      "domains": [
        "JobPosting"
      ], 
      "id": "employmentType", 
      "label": "Employment Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "encodesCreativeWork": {
      "comment": "The creative work encoded by this media object", 
      "comment_plain": "The creative work encoded by this media object", 
      "domains": [
        "MediaObject"
      ], 
      "id": "encodesCreativeWork", 
      "label": "Encodes Creative Work", 
      "ranges": [
        "CreativeWork"
      ]
    }, 
    "encoding": {
      "comment": "A media object that encode this CreativeWork.", 
      "comment_plain": "A media object that encode this CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "encoding", 
      "label": "Encoding", 
      "ranges": [
        "MediaObject"
      ]
    }, 
    "encodingFormat": {
      "comment": "mp3, mpeg4, etc.", 
      "comment_plain": "mp3, mpeg4, etc.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "encodingFormat", 
      "label": "Encoding Format", 
      "ranges": [
        "Text"
      ]
    }, 
    "encodings": {
      "comment": "The media objects that encode this creative work (legacy spelling; see singular form, encoding).", 
      "comment_plain": "The media objects that encode this creative work (legacy spelling; see singular form, encoding).", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "encodings", 
      "label": "Encodings", 
      "ranges": [
        "MediaObject"
      ]
    }, 
    "endDate": {
      "comment": "The end date and time of the event (in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 date format</a>).", 
      "comment_plain": "The end date and time of the event (in ISO 8601 date format).", 
      "domains": [
        "TVSeason", 
        "Event", 
        "TVSeries"
      ], 
      "id": "endDate", 
      "label": "End Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "endorsers": {
      "comment": "People or organizations that endorse the plan.", 
      "comment_plain": "People or organizations that endorse the plan.", 
      "domains": [
        "Diet"
      ], 
      "id": "endorsers", 
      "label": "Endorsers", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "epidemiology": {
      "comment": "The characteristics of associated patients, such as age, gender, race etc.", 
      "comment_plain": "The characteristics of associated patients, such as age, gender, race etc.", 
      "domains": [
        "MedicalCondition", 
        "PhysicalActivity"
      ], 
      "id": "epidemiology", 
      "label": "Epidemiology", 
      "ranges": [
        "Text"
      ]
    }, 
    "episode": {
      "comment": "An episode of a TV series or season.", 
      "comment_plain": "An episode of a TV series or season.", 
      "domains": [
        "TVSeason", 
        "TVSeries"
      ], 
      "id": "episode", 
      "label": "Episode", 
      "ranges": [
        "TVEpisode"
      ]
    }, 
    "episodeNumber": {
      "comment": "The episode number.", 
      "comment_plain": "The episode number.", 
      "domains": [
        "TVEpisode"
      ], 
      "id": "episodeNumber", 
      "label": "Episode Number", 
      "ranges": [
        "Number"
      ]
    }, 
    "episodes": {
      "comment": "The episode of a TV series or season (legacy spelling; see singular form, episode).", 
      "comment_plain": "The episode of a TV series or season (legacy spelling; see singular form, episode).", 
      "domains": [
        "TVSeason", 
        "TVSeries"
      ], 
      "id": "episodes", 
      "label": "Episodes", 
      "ranges": [
        "TVEpisode"
      ]
    }, 
    "equal": {
      "comment": "This ordering relation for qualitative values indicates that the subject is equal to the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is equal to the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "equal", 
      "label": "Equal", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "estimatesRiskOf": {
      "comment": "The condition, complication, or symptom whose risk is being estimated.", 
      "comment_plain": "The condition, complication, or symptom whose risk is being estimated.", 
      "domains": [
        "MedicalRiskEstimator"
      ], 
      "id": "estimatesRiskOf", 
      "label": "Estimates Risk of", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "event": {
      "comment": "Upcoming or past event associated with this place or organization.", 
      "comment_plain": "Upcoming or past event associated with this place or organization.", 
      "domains": [
        "Organization", 
        "Place"
      ], 
      "id": "event", 
      "label": "Event", 
      "ranges": [
        "Event"
      ]
    }, 
    "events": {
      "comment": "Upcoming or past events associated with this place or organization (legacy spelling; see singular form, event).", 
      "comment_plain": "Upcoming or past events associated with this place or organization (legacy spelling; see singular form, event).", 
      "domains": [
        "Organization", 
        "Place"
      ], 
      "id": "events", 
      "label": "Events", 
      "ranges": [
        "Event"
      ]
    }, 
    "evidenceLevel": {
      "comment": "Strength of evidence of the data used to formulate the guideline (enumerated).", 
      "comment_plain": "Strength of evidence of the data used to formulate the guideline (enumerated).", 
      "domains": [
        "MedicalGuideline"
      ], 
      "id": "evidenceLevel", 
      "label": "Evidence Level", 
      "ranges": [
        "MedicalEvidenceLevel"
      ]
    }, 
    "evidenceOrigin": {
      "comment": "Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.", 
      "comment_plain": "Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.", 
      "domains": [
        "MedicalGuideline"
      ], 
      "id": "evidenceOrigin", 
      "label": "Evidence Origin", 
      "ranges": [
        "Text"
      ]
    }, 
    "exerciseType": {
      "comment": "Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.", 
      "comment_plain": "Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "exerciseType", 
      "label": "Exercise Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "exifData": {
      "comment": "exif data for this object.", 
      "comment_plain": "exif data for this object.", 
      "domains": [
        "ImageObject"
      ], 
      "id": "exifData", 
      "label": "Exif Data", 
      "ranges": [
        "Text"
      ]
    }, 
    "expectedPrognosis": {
      "comment": "The likely outcome in either the short term or long term of the medical condition.", 
      "comment_plain": "The likely outcome in either the short term or long term of the medical condition.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "expectedPrognosis", 
      "label": "Expected Prognosis", 
      "ranges": [
        "Text"
      ]
    }, 
    "experienceRequirements": {
      "comment": "Description of skills and experience needed for the position.", 
      "comment_plain": "Description of skills and experience needed for the position.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "experienceRequirements", 
      "label": "Experience Requirements", 
      "ranges": [
        "Text"
      ]
    }, 
    "expertConsiderations": {
      "comment": "Medical expert advice related to the plan.", 
      "comment_plain": "Medical expert advice related to the plan.", 
      "domains": [
        "Diet"
      ], 
      "id": "expertConsiderations", 
      "label": "Expert Considerations", 
      "ranges": [
        "Text"
      ]
    }, 
    "expires": {
      "comment": "Date the content expires and is no longer useful or available. Useful for videos.", 
      "comment_plain": "Date the content expires and is no longer useful or available. Useful for videos.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "expires", 
      "label": "Expires", 
      "ranges": [
        "Date"
      ]
    }, 
    "familyName": {
      "comment": "Family name. In the U.S., the last name of an Person. This can be used along with givenName instead of the Name property.", 
      "comment_plain": "Family name. In the U.S., the last name of an Person. This can be used along with givenName instead of the Name property.", 
      "domains": [
        "Person"
      ], 
      "id": "familyName", 
      "label": "Family Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "fatContent": {
      "comment": "The number of grams of fat.", 
      "comment_plain": "The number of grams of fat.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "fatContent", 
      "label": "Fat Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "faxNumber": {
      "comment": "The fax number.", 
      "comment_plain": "The fax number.", 
      "domains": [
        "Organization", 
        "ContactPoint", 
        "Place", 
        "Person"
      ], 
      "id": "faxNumber", 
      "label": "Fax Number", 
      "ranges": [
        "Text"
      ]
    }, 
    "featureList": {
      "comment": "Features or modules provided by this application (and possibly required by other applications).", 
      "comment_plain": "Features or modules provided by this application (and possibly required by other applications).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "featureList", 
      "label": "Feature List", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "fiberContent": {
      "comment": "The number of grams of fiber.", 
      "comment_plain": "The number of grams of fiber.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "fiberContent", 
      "label": "Fiber Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "fileFormat": {
      "comment": "MIME format of the binary (e.g. application/zip).", 
      "comment_plain": "MIME format of the binary (e.g. application/zip).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "fileFormat", 
      "label": "File Format", 
      "ranges": [
        "Text"
      ]
    }, 
    "fileSize": {
      "comment": "Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.", 
      "comment_plain": "Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "fileSize", 
      "label": "File Size", 
      "ranges": [
        "Integer"
      ]
    }, 
    "follows": {
      "comment": "The most generic uni-directional social relation.", 
      "comment_plain": "The most generic uni-directional social relation.", 
      "domains": [
        "Person"
      ], 
      "id": "follows", 
      "label": "Follows", 
      "ranges": [
        "Person"
      ]
    }, 
    "followup": {
      "comment": "Typical or recommended followup care after the procedure is performed.", 
      "comment_plain": "Typical or recommended followup care after the procedure is performed.", 
      "domains": [
        "MedicalProcedure"
      ], 
      "id": "followup", 
      "label": "Followup", 
      "ranges": [
        "Text"
      ]
    }, 
    "foodWarning": {
      "comment": "Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.", 
      "comment_plain": "Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.", 
      "domains": [
        "Drug"
      ], 
      "id": "foodWarning", 
      "label": "Food Warning", 
      "ranges": [
        "Text"
      ]
    }, 
    "founder": {
      "comment": "A person who founded this organization.", 
      "comment_plain": "A person who founded this organization.", 
      "domains": [
        "Organization"
      ], 
      "id": "founder", 
      "label": "Founder", 
      "ranges": [
        "Person"
      ]
    }, 
    "founders": {
      "comment": "A person who founded this organization (legacy spelling; see singular form, founder).", 
      "comment_plain": "A person who founded this organization (legacy spelling; see singular form, founder).", 
      "domains": [
        "Organization"
      ], 
      "id": "founders", 
      "label": "Founders", 
      "ranges": [
        "Person"
      ]
    }, 
    "foundingDate": {
      "comment": "The date that this organization was founded.", 
      "comment_plain": "The date that this organization was founded.", 
      "domains": [
        "Organization"
      ], 
      "id": "foundingDate", 
      "label": "Founding Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "frequency": {
      "comment": "How often the dose is taken, e.g. 'daily'.", 
      "comment_plain": "How often the dose is taken, e.g. 'daily'.", 
      "domains": [
        "DoseSchedule"
      ], 
      "id": "frequency", 
      "label": "Frequency", 
      "ranges": [
        "Text"
      ]
    }, 
    "function": {
      "comment": "Function of the anatomical structure.", 
      "comment_plain": "Function of the anatomical structure.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "function", 
      "label": "Function", 
      "ranges": [
        "Text"
      ]
    }, 
    "functionalClass": {
      "comment": "The degree of mobility the joint allows.", 
      "comment_plain": "The degree of mobility the joint allows.", 
      "domains": [
        "Joint"
      ], 
      "id": "functionalClass", 
      "label": "Functional Class", 
      "ranges": [
        "Text"
      ]
    }, 
    "gender": {
      "comment": "Gender of the person.", 
      "comment_plain": "Gender of the person.", 
      "domains": [
        "Person"
      ], 
      "id": "gender", 
      "label": "Gender", 
      "ranges": [
        "Text"
      ]
    }, 
    "genre": {
      "comment": "Genre of the creative work", 
      "comment_plain": "Genre of the creative work", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "genre", 
      "label": "Genre", 
      "ranges": [
        "Text"
      ]
    }, 
    "geo": {
      "comment": "The geo coordinates of the place.", 
      "comment_plain": "The geo coordinates of the place.", 
      "domains": [
        "Place"
      ], 
      "id": "geo", 
      "label": "Geo", 
      "ranges": [
        "GeoCoordinates", 
        "GeoShape"
      ]
    }, 
    "givenName": {
      "comment": "Given name. In the U.S., the first name of a Person. This can be used along with familyName instead of the Name property.", 
      "comment_plain": "Given name. In the U.S., the first name of a Person. This can be used along with familyName instead of the Name property.", 
      "domains": [
        "Person"
      ], 
      "id": "givenName", 
      "label": "Given Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "globalLocationNumber": {
      "comment": "The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.", 
      "comment_plain": "The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.", 
      "domains": [
        "Organization", 
        "Place", 
        "Person"
      ], 
      "id": "globalLocationNumber", 
      "label": "Global Location Number", 
      "ranges": [
        "Text"
      ]
    }, 
    "greater": {
      "comment": "This ordering relation for qualitative values indicates that the subject is greater than the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is greater than the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "greater", 
      "label": "Greater", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "greaterOrEqual": {
      "comment": "This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "greaterOrEqual", 
      "label": "Greater or Equal", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "gtin13": {
      "comment": "The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero.", 
      "comment_plain": "The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "gtin13", 
      "label": "Gtin13", 
      "ranges": [
        "Text"
      ]
    }, 
    "gtin14": {
      "comment": "The GTIN-14 code of the product, or the product to which the offer refers.", 
      "comment_plain": "The GTIN-14 code of the product, or the product to which the offer refers.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "gtin14", 
      "label": "Gtin14", 
      "ranges": [
        "Text"
      ]
    }, 
    "gtin8": {
      "comment": "The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN.", 
      "comment_plain": "The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "gtin8", 
      "label": "Gtin8", 
      "ranges": [
        "Text"
      ]
    }, 
    "guideline": {
      "comment": "A medical guideline related to this entity.", 
      "comment_plain": "A medical guideline related to this entity.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "guideline", 
      "label": "Guideline", 
      "ranges": [
        "MedicalGuideline"
      ]
    }, 
    "guidelineDate": {
      "comment": "Date on which this guideline's recommendation was made.", 
      "comment_plain": "Date on which this guideline's recommendation was made.", 
      "domains": [
        "MedicalGuideline"
      ], 
      "id": "guidelineDate", 
      "label": "Guideline Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "guidelineSubject": {
      "comment": "The medical conditions, treatments, etc. that are the subject of the guideline.", 
      "comment_plain": "The medical conditions, treatments, etc. that are the subject of the guideline.", 
      "domains": [
        "MedicalGuideline"
      ], 
      "id": "guidelineSubject", 
      "label": "Guideline Subject", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "hasPOS": {
      "comment": "Points-of-Sales operated by the organization or person.", 
      "comment_plain": "Points-of-Sales operated by the organization or person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "hasPOS", 
      "label": "Has POS", 
      "ranges": [
        "Place"
      ]
    }, 
    "headline": {
      "comment": "Headline of the article", 
      "comment_plain": "Headline of the article", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "headline", 
      "label": "Headline", 
      "ranges": [
        "Text"
      ]
    }, 
    "healthCondition": {
      "comment": "Expectations for health conditions of target audience", 
      "comment_plain": "Expectations for health conditions of target audience", 
      "domains": [
        "PeopleAudience"
      ], 
      "id": "healthCondition", 
      "label": "Health Condition", 
      "ranges": [
        "MedicalCondition"
      ]
    }, 
    "height": {
      "comment": "The height of the item.", 
      "comment_plain": "The height of the item.", 
      "domains": [
        "MediaObject", 
        "Product"
      ], 
      "id": "height", 
      "label": "Height", 
      "ranges": [
        "Distance", 
        "QuantitativeValue"
      ]
    }, 
    "highPrice": {
      "comment": "The highest price of all offers available.", 
      "comment_plain": "The highest price of all offers available.", 
      "domains": [
        "AggregateOffer"
      ], 
      "id": "highPrice", 
      "label": "High Price", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "hiringOrganization": {
      "comment": "Organization offering the job position.", 
      "comment_plain": "Organization offering the job position.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "hiringOrganization", 
      "label": "Hiring Organization", 
      "ranges": [
        "Organization"
      ]
    }, 
    "homeLocation": {
      "comment": "A contact location for a person's residence.", 
      "comment_plain": "A contact location for a person's residence.", 
      "domains": [
        "Person"
      ], 
      "id": "homeLocation", 
      "label": "Home Location", 
      "ranges": [
        "ContactPoint", 
        "Place"
      ]
    }, 
    "honorificPrefix": {
      "comment": "An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.", 
      "comment_plain": "An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.", 
      "domains": [
        "Person"
      ], 
      "id": "honorificPrefix", 
      "label": "Honorific Prefix", 
      "ranges": [
        "Text"
      ]
    }, 
    "honorificSuffix": {
      "comment": "An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.", 
      "comment_plain": "An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.", 
      "domains": [
        "Person"
      ], 
      "id": "honorificSuffix", 
      "label": "Honorific Suffix", 
      "ranges": [
        "Text"
      ]
    }, 
    "hospitalAffiliation": {
      "comment": "A hospital with which the physician or office is affiliated.", 
      "comment_plain": "A hospital with which the physician or office is affiliated.", 
      "domains": [
        "Physician"
      ], 
      "id": "hospitalAffiliation", 
      "label": "Hospital Affiliation", 
      "ranges": [
        "Hospital"
      ]
    }, 
    "howPerformed": {
      "comment": "How the procedure is performed.", 
      "comment_plain": "How the procedure is performed.", 
      "domains": [
        "MedicalProcedure"
      ], 
      "id": "howPerformed", 
      "label": "How Performed", 
      "ranges": [
        "Text"
      ]
    }, 
    "identifyingExam": {
      "comment": "A physical examination that can identify this sign.", 
      "comment_plain": "A physical examination that can identify this sign.", 
      "domains": [
        "MedicalSign"
      ], 
      "id": "identifyingExam", 
      "label": "Identifying Exam", 
      "ranges": [
        "PhysicalExam"
      ]
    }, 
    "identifyingTest": {
      "comment": "A diagnostic test that can identify this sign.", 
      "comment_plain": "A diagnostic test that can identify this sign.", 
      "domains": [
        "MedicalSign"
      ], 
      "id": "identifyingTest", 
      "label": "Identifying Test", 
      "ranges": [
        "MedicalTest"
      ]
    }, 
    "illustrator": {
      "comment": "The illustrator of the book.", 
      "comment_plain": "The illustrator of the book.", 
      "domains": [
        "Book"
      ], 
      "id": "illustrator", 
      "label": "Illustrator", 
      "ranges": [
        "Person"
      ]
    }, 
    "image": {
      "comment": "URL of an image of the item.", 
      "comment_plain": "URL of an image of the item.", 
      "domains": [
        "Thing"
      ], 
      "id": "image", 
      "label": "Image", 
      "ranges": [
        "URL"
      ]
    }, 
    "imagingTechnique": {
      "comment": "Imaging technique used.", 
      "comment_plain": "Imaging technique used.", 
      "domains": [
        "ImagingTest"
      ], 
      "id": "imagingTechnique", 
      "label": "Imaging Technique", 
      "ranges": [
        "MedicalImagingTechnique"
      ]
    }, 
    "inAlbum": {
      "comment": "The album to which this recording belongs.", 
      "comment_plain": "The album to which this recording belongs.", 
      "domains": [
        "MusicRecording"
      ], 
      "id": "inAlbum", 
      "label": "In Album", 
      "ranges": [
        "MusicAlbum"
      ]
    }, 
    "inLanguage": {
      "comment": "The language of the content. please use one of the language codes from the <a href=\"http://tools.ietf.org/html/bcp47\">IETF BCP 47 standard.</a>", 
      "comment_plain": "The language of the content. please use one of the language codes from the IETF BCP 47 standard.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "inLanguage", 
      "label": "In Language", 
      "ranges": [
        "Text"
      ]
    }, 
    "inPlaylist": {
      "comment": "The playlist to which this recording belongs.", 
      "comment_plain": "The playlist to which this recording belongs.", 
      "domains": [
        "MusicRecording"
      ], 
      "id": "inPlaylist", 
      "label": "In Playlist", 
      "ranges": [
        "MusicPlaylist"
      ]
    }, 
    "incentives": {
      "comment": "Description of bonus and commission compensation aspects of the job.", 
      "comment_plain": "Description of bonus and commission compensation aspects of the job.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "incentives", 
      "label": "Incentives", 
      "ranges": [
        "Text"
      ]
    }, 
    "includedRiskFactor": {
      "comment": "A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.", 
      "comment_plain": "A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.", 
      "domains": [
        "MedicalRiskEstimator"
      ], 
      "id": "includedRiskFactor", 
      "label": "Included Risk Factor", 
      "ranges": [
        "MedicalRiskFactor"
      ]
    }, 
    "includesObject": {
      "comment": "This links to a node or nodes indicating the exact quantity of the products included in the offer.", 
      "comment_plain": "This links to a node or nodes indicating the exact quantity of the products included in the offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "includesObject", 
      "label": "Includes Object", 
      "ranges": [
        "TypeAndQuantityNode"
      ]
    }, 
    "increasesRiskOf": {
      "comment": "The condition, complication, etc. influenced by this factor.", 
      "comment_plain": "The condition, complication, etc. influenced by this factor.", 
      "domains": [
        "MedicalRiskFactor"
      ], 
      "id": "increasesRiskOf", 
      "label": "Increases Risk of", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "indication": {
      "comment": "A factor that indicates use of this therapy for treatment and/or prevention of a condition, symptom, etc. For therapies such as drugs, indications can include both officially-approved indications as well as off-label uses. These can be distinguished by using the ApprovedIndication subtype of MedicalIndication.", 
      "comment_plain": "A factor that indicates use of this therapy for treatment and/or prevention of a condition, symptom, etc. For therapies such as drugs, indications can include both officially-approved indications as well as off-label uses. These can be distinguished by using the ApprovedIndication subtype of MedicalIndication.", 
      "domains": [
        "MedicalDevice", 
        "MedicalTherapy"
      ], 
      "id": "indication", 
      "label": "Indication", 
      "ranges": [
        "MedicalIndication"
      ]
    }, 
    "industry": {
      "comment": "The industry associated with the job position.", 
      "comment_plain": "The industry associated with the job position.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "industry", 
      "label": "Industry", 
      "ranges": [
        "Text"
      ]
    }, 
    "infectiousAgent": {
      "comment": "The actual infectious agent, such as a specific bacterium.", 
      "comment_plain": "The actual infectious agent, such as a specific bacterium.", 
      "domains": [
        "InfectiousDisease"
      ], 
      "id": "infectiousAgent", 
      "label": "Infectious Agent", 
      "ranges": [
        "Text"
      ]
    }, 
    "infectiousAgentClass": {
      "comment": "The class of infectious agent (bacteria, prion, etc.) that causes the disease.", 
      "comment_plain": "The class of infectious agent (bacteria, prion, etc.) that causes the disease.", 
      "domains": [
        "InfectiousDisease"
      ], 
      "id": "infectiousAgentClass", 
      "label": "Infectious Agent Class", 
      "ranges": [
        "InfectiousAgentClass"
      ]
    }, 
    "ingredients": {
      "comment": "An ingredient used in the recipe.", 
      "comment_plain": "An ingredient used in the recipe.", 
      "domains": [
        "Recipe"
      ], 
      "id": "ingredients", 
      "label": "Ingredients", 
      "ranges": [
        "Text"
      ]
    }, 
    "insertion": {
      "comment": "The place of attachment of a muscle, or what the muscle moves.", 
      "comment_plain": "The place of attachment of a muscle, or what the muscle moves.", 
      "domains": [
        "Muscle"
      ], 
      "id": "insertion", 
      "label": "Insertion", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "installUrl": {
      "comment": "URL at which the app may be installed, if different from the URL of the item.", 
      "comment_plain": "URL at which the app may be installed, if different from the URL of the item.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "installUrl", 
      "label": "Install Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "intensity": {
      "comment": "Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.", 
      "comment_plain": "Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "intensity", 
      "label": "Intensity", 
      "ranges": [
        "Text"
      ]
    }, 
    "interactingDrug": {
      "comment": "Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.", 
      "comment_plain": "Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.", 
      "domains": [
        "Drug"
      ], 
      "id": "interactingDrug", 
      "label": "Interacting Drug", 
      "ranges": [
        "Drug"
      ]
    }, 
    "interactionCount": {
      "comment": "A count of a specific user interactions with this item\u2014for example, <code>20 UserLikes</code>, <code>5 UserComments</code>, or <code>300 UserDownloads</code>. The user interaction type should be one of the sub types of <a href=\"http://schema.org/UserInteraction\">UserInteraction</a>.", 
      "comment_plain": "A count of a specific user interactions with this item\u2014for example, 20 UserLikes, 5 UserComments, or 300 UserDownloads. The user interaction type should be one of the sub types of UserInteraction.", 
      "domains": [
        "Organization", 
        "CreativeWork", 
        "Place", 
        "Person"
      ], 
      "id": "interactionCount", 
      "label": "Interaction Count", 
      "ranges": [
        "Text"
      ]
    }, 
    "interactivityType": {
      "comment": "The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.", 
      "comment_plain": "The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "interactivityType", 
      "label": "Interactivity Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "inventoryLevel": {
      "comment": "The current approximate inventory level for the item or items.", 
      "comment_plain": "The current approximate inventory level for the item or items.", 
      "domains": [
        "SomeProducts", 
        "Offer", 
        "Demand"
      ], 
      "id": "inventoryLevel", 
      "label": "Inventory Level", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "isAccessoryOrSparePartFor": {
      "comment": "A pointer to another product (or multiple products) for which this product is an accessory or spare part.", 
      "comment_plain": "A pointer to another product (or multiple products) for which this product is an accessory or spare part.", 
      "domains": [
        "Product"
      ], 
      "id": "isAccessoryOrSparePartFor", 
      "label": "Is Accessory or Spare Part for", 
      "ranges": [
        "Product"
      ]
    }, 
    "isAvailableGenerically": {
      "comment": "True if the drug is available in a generic form (regardless of name).", 
      "comment_plain": "True if the drug is available in a generic form (regardless of name).", 
      "domains": [
        "Drug"
      ], 
      "id": "isAvailableGenerically", 
      "label": "Is Available Generically", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "isBasedOnUrl": {
      "comment": "A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html", 
      "comment_plain": "A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "isBasedOnUrl", 
      "label": "Is Based On Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "isConsumableFor": {
      "comment": "A pointer to another product (or multiple products) for which this product is a consumable.", 
      "comment_plain": "A pointer to another product (or multiple products) for which this product is a consumable.", 
      "domains": [
        "Product"
      ], 
      "id": "isConsumableFor", 
      "label": "Is Consumable for", 
      "ranges": [
        "Product"
      ]
    }, 
    "isFamilyFriendly": {
      "comment": "Indicates whether this content is family friendly.", 
      "comment_plain": "Indicates whether this content is family friendly.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "isFamilyFriendly", 
      "label": "Is Family Friendly", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "isPartOf": {
      "comment": "Indicates the collection or gallery to which the item belongs.", 
      "comment_plain": "Indicates the collection or gallery to which the item belongs.", 
      "domains": [
        "WebPage"
      ], 
      "id": "isPartOf", 
      "label": "Is Part of", 
      "ranges": [
        "CollectionPage"
      ]
    }, 
    "isProprietary": {
      "comment": "True if this item's name is a proprietary/brand name (vs. generic name).", 
      "comment_plain": "True if this item's name is a proprietary/brand name (vs. generic name).", 
      "domains": [
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "isProprietary", 
      "label": "Is Proprietary", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "isRelatedTo": {
      "comment": "A pointer to another, somehow related product (or multiple products).", 
      "comment_plain": "A pointer to another, somehow related product (or multiple products).", 
      "domains": [
        "Product"
      ], 
      "id": "isRelatedTo", 
      "label": "Is Related to", 
      "ranges": [
        "Product"
      ]
    }, 
    "isSimilarTo": {
      "comment": "A pointer to another, functionally similar product (or multiple products).", 
      "comment_plain": "A pointer to another, functionally similar product (or multiple products).", 
      "domains": [
        "Product"
      ], 
      "id": "isSimilarTo", 
      "label": "Is Similar to", 
      "ranges": [
        "Product"
      ]
    }, 
    "isVariantOf": {
      "comment": "A pointer to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive.", 
      "comment_plain": "A pointer to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive.", 
      "domains": [
        "ProductModel"
      ], 
      "id": "isVariantOf", 
      "label": "Is Variant of", 
      "ranges": [
        "ProductModel"
      ]
    }, 
    "isbn": {
      "comment": "The ISBN of the book.", 
      "comment_plain": "The ISBN of the book.", 
      "domains": [
        "Book"
      ], 
      "id": "isbn", 
      "label": "ISBN", 
      "ranges": [
        "Text"
      ]
    }, 
    "isicV4": {
      "comment": "The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.", 
      "comment_plain": "The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.", 
      "domains": [
        "Organization", 
        "Place", 
        "Person"
      ], 
      "id": "isicV4", 
      "label": "Isic V4", 
      "ranges": [
        "Text"
      ]
    }, 
    "itemCondition": {
      "comment": "A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.", 
      "comment_plain": "A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "itemCondition", 
      "label": "Item Condition", 
      "ranges": [
        "OfferItemCondition"
      ]
    }, 
    "itemListElement": {
      "comment": "A single list item.", 
      "comment_plain": "A single list item.", 
      "domains": [
        "ItemList"
      ], 
      "id": "itemListElement", 
      "label": "Item List Element", 
      "ranges": [
        "Text"
      ]
    }, 
    "itemListOrder": {
      "comment": "Type of ordering (e.g. Ascending, Descending, Unordered).", 
      "comment_plain": "Type of ordering (e.g. Ascending, Descending, Unordered).", 
      "domains": [
        "ItemList"
      ], 
      "id": "itemListOrder", 
      "label": "Item List Order", 
      "ranges": [
        "Text"
      ]
    }, 
    "itemOffered": {
      "comment": "The item being sold.", 
      "comment_plain": "The item being sold.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "itemOffered", 
      "label": "Item Offered", 
      "ranges": [
        "Product"
      ]
    }, 
    "itemReviewed": {
      "comment": "The item that is being reviewed/rated.", 
      "comment_plain": "The item that is being reviewed/rated.", 
      "domains": [
        "AggregateRating", 
        "Review"
      ], 
      "id": "itemReviewed", 
      "label": "Item Reviewed", 
      "ranges": [
        "Thing"
      ]
    }, 
    "jobLocation": {
      "comment": "A (typically single) geographic location associated with the job position.", 
      "comment_plain": "A (typically single) geographic location associated with the job position.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "jobLocation", 
      "label": "Job Location", 
      "ranges": [
        "Place"
      ]
    }, 
    "jobTitle": {
      "comment": "The job title of the person (for example, Financial Manager).", 
      "comment_plain": "The job title of the person (for example, Financial Manager).", 
      "domains": [
        "Person"
      ], 
      "id": "jobTitle", 
      "label": "Job Title", 
      "ranges": [
        "Text"
      ]
    }, 
    "keywords": {
      "comment": "The keywords/tags used to describe this content.", 
      "comment_plain": "The keywords/tags used to describe this content.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "keywords", 
      "label": "Keywords", 
      "ranges": [
        "Text"
      ]
    }, 
    "knows": {
      "comment": "The most generic bi-directional social/work relation.", 
      "comment_plain": "The most generic bi-directional social/work relation.", 
      "domains": [
        "Person"
      ], 
      "id": "knows", 
      "label": "Knows", 
      "ranges": [
        "Person"
      ]
    }, 
    "labelDetails": {
      "comment": "Link to the drug's label details.", 
      "comment_plain": "Link to the drug's label details.", 
      "domains": [
        "Drug"
      ], 
      "id": "labelDetails", 
      "label": "Label Details", 
      "ranges": [
        "URL"
      ]
    }, 
    "lastReviewed": {
      "comment": "Date on which the content on this web page was last reviewed for accuracy and/or completeness.", 
      "comment_plain": "Date on which the content on this web page was last reviewed for accuracy and/or completeness.", 
      "domains": [
        "WebPage"
      ], 
      "id": "lastReviewed", 
      "label": "Last Reviewed", 
      "ranges": [
        "Date"
      ]
    }, 
    "latitude": {
      "comment": "The latitude of a location. For example <code>37.42242</code>.", 
      "comment_plain": "The latitude of a location. For example 37.42242.", 
      "domains": [
        "GeoCoordinates"
      ], 
      "id": "latitude", 
      "label": "Latitude", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "learningResourceType": {
      "comment": "The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.", 
      "comment_plain": "The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "learningResourceType", 
      "label": "Learning Resource Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "legalName": {
      "comment": "The official name of the organization, e.g. the registered company name.", 
      "comment_plain": "The official name of the organization, e.g. the registered company name.", 
      "domains": [
        "Organization"
      ], 
      "id": "legalName", 
      "label": "Legal Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "legalStatus": {
      "comment": "The drug or supplement's legal status, including any controlled substance schedules that apply.", 
      "comment_plain": "The drug or supplement's legal status, including any controlled substance schedules that apply.", 
      "domains": [
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "legalStatus", 
      "label": "Legal Status", 
      "ranges": [
        "DrugLegalStatus"
      ]
    }, 
    "lesser": {
      "comment": "This ordering relation for qualitative values indicates that the subject is lesser than the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is lesser than the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "lesser", 
      "label": "Lesser", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "lesserOrEqual": {
      "comment": "This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "lesserOrEqual", 
      "label": "Lesser or Equal", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "line": {
      "comment": "A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.", 
      "comment_plain": "A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.", 
      "domains": [
        "GeoShape"
      ], 
      "id": "line", 
      "label": "Line", 
      "ranges": [
        "Text"
      ]
    }, 
    "location": {
      "comment": "The location of the event or organization.", 
      "comment_plain": "The location of the event or organization.", 
      "domains": [
        "Organization", 
        "Event"
      ], 
      "id": "location", 
      "label": "Location", 
      "ranges": [
        "PostalAddress", 
        "Place"
      ]
    }, 
    "logo": {
      "comment": "URL of an image for the logo of the item.", 
      "comment_plain": "URL of an image for the logo of the item.", 
      "domains": [
        "Organization", 
        "Brand", 
        "Place", 
        "Product"
      ], 
      "id": "logo", 
      "label": "Logo", 
      "ranges": [
        "URL", 
        "ImageObject"
      ]
    }, 
    "longitude": {
      "comment": "The longitude of a location. For example <code>-122.08585</code>.", 
      "comment_plain": "The longitude of a location. For example -122.08585.", 
      "domains": [
        "GeoCoordinates"
      ], 
      "id": "longitude", 
      "label": "Longitude", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "lowPrice": {
      "comment": "The lowest price of all offers available.", 
      "comment_plain": "The lowest price of all offers available.", 
      "domains": [
        "AggregateOffer"
      ], 
      "id": "lowPrice", 
      "label": "Low Price", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }, 
    "mainContentOfPage": {
      "comment": "Indicates if this web page element is the main subject of the page.", 
      "comment_plain": "Indicates if this web page element is the main subject of the page.", 
      "domains": [
        "WebPage"
      ], 
      "id": "mainContentOfPage", 
      "label": "Main Content of Page", 
      "ranges": [
        "WebPageElement"
      ]
    }, 
    "makesOffer": {
      "comment": "A pointer to products or services offered by the organization or person.", 
      "comment_plain": "A pointer to products or services offered by the organization or person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "makesOffer", 
      "label": "Makes Offer", 
      "ranges": [
        "Offer"
      ]
    }, 
    "manufacturer": {
      "comment": "The manufacturer of the product.", 
      "comment_plain": "The manufacturer of the product.", 
      "domains": [
        "Product", 
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "manufacturer", 
      "label": "Manufacturer", 
      "ranges": [
        "Organization"
      ]
    }, 
    "map": {
      "comment": "A URL to a map of the place.", 
      "comment_plain": "A URL to a map of the place.", 
      "domains": [
        "Place"
      ], 
      "id": "map", 
      "label": "Map", 
      "ranges": [
        "URL"
      ]
    }, 
    "maps": {
      "comment": "A URL to a map of the place (legacy spelling; see singular form, map).", 
      "comment_plain": "A URL to a map of the place (legacy spelling; see singular form, map).", 
      "domains": [
        "Place"
      ], 
      "id": "maps", 
      "label": "Maps", 
      "ranges": [
        "URL"
      ]
    }, 
    "maxPrice": {
      "comment": "The highest price if the price is a range.", 
      "comment_plain": "The highest price if the price is a range.", 
      "domains": [
        "PriceSpecification"
      ], 
      "id": "maxPrice", 
      "label": "Max Price", 
      "ranges": [
        "Number"
      ]
    }, 
    "maxValue": {
      "comment": "The upper of the product characteristic.", 
      "comment_plain": "The upper of the product characteristic.", 
      "domains": [
        "QuantitativeValue"
      ], 
      "id": "maxValue", 
      "label": "Max Value", 
      "ranges": [
        "Number"
      ]
    }, 
    "maximumIntake": {
      "comment": "Recommended intake of this supplement for a given population as defined by a specific recommending authority.", 
      "comment_plain": "Recommended intake of this supplement for a given population as defined by a specific recommending authority.", 
      "domains": [
        "DietarySupplement"
      ], 
      "id": "maximumIntake", 
      "label": "Maximum Intake", 
      "ranges": [
        "MaximumDoseSchedule"
      ]
    }, 
    "mechanismOfAction": {
      "comment": "The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.", 
      "comment_plain": "The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.", 
      "domains": [
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "mechanismOfAction", 
      "label": "Mechanism of Action", 
      "ranges": [
        "Text"
      ]
    }, 
    "medicalSpecialty": {
      "comment": "A medical specialty of the provider.", 
      "comment_plain": "A medical specialty of the provider.", 
      "domains": [
        "Physician", 
        "Hospital", 
        "MedicalClinic"
      ], 
      "id": "medicalSpecialty", 
      "label": "Medical Specialty", 
      "ranges": [
        "MedicalSpecialty"
      ]
    }, 
    "medicineSystem": {
      "comment": "The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.", 
      "comment_plain": "The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "medicineSystem", 
      "label": "Medicine System", 
      "ranges": [
        "MedicineSystem"
      ]
    }, 
    "member": {
      "comment": "A member of this organization.", 
      "comment_plain": "A member of this organization.", 
      "domains": [
        "Organization"
      ], 
      "id": "member", 
      "label": "Member", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "memberOf": {
      "comment": "An organization to which the person belongs.", 
      "comment_plain": "An organization to which the person belongs.", 
      "domains": [
        "Person"
      ], 
      "id": "memberOf", 
      "label": "Member of", 
      "ranges": [
        "Organization"
      ]
    }, 
    "members": {
      "comment": "A member of this organization (legacy spelling; see singular form, member).", 
      "comment_plain": "A member of this organization (legacy spelling; see singular form, member).", 
      "domains": [
        "Organization"
      ], 
      "id": "members", 
      "label": "Members", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "memoryRequirements": {
      "comment": "Minimum memory requirements.", 
      "comment_plain": "Minimum memory requirements.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "memoryRequirements", 
      "label": "Memory Requirements", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "mentions": {
      "comment": "Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.", 
      "comment_plain": "Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "mentions", 
      "label": "Mentions", 
      "ranges": [
        "Thing"
      ]
    }, 
    "menu": {
      "comment": "Either the actual menu or a URL of the menu.", 
      "comment_plain": "Either the actual menu or a URL of the menu.", 
      "domains": [
        "FoodEstablishment"
      ], 
      "id": "menu", 
      "label": "Menu", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "minPrice": {
      "comment": "The lowest price if the price is a range.", 
      "comment_plain": "The lowest price if the price is a range.", 
      "domains": [
        "PriceSpecification"
      ], 
      "id": "minPrice", 
      "label": "Min Price", 
      "ranges": [
        "Number"
      ]
    }, 
    "minValue": {
      "comment": "The lower value of the product characteristic.", 
      "comment_plain": "The lower value of the product characteristic.", 
      "domains": [
        "QuantitativeValue"
      ], 
      "id": "minValue", 
      "label": "Min Value", 
      "ranges": [
        "Number"
      ]
    }, 
    "model": {
      "comment": "The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.", 
      "comment_plain": "The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.", 
      "domains": [
        "Product"
      ], 
      "id": "model", 
      "label": "Model", 
      "ranges": [
        "ProductModel", 
        "Text"
      ]
    }, 
    "mpn": {
      "comment": "The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.", 
      "comment_plain": "The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "mpn", 
      "label": "Mpn", 
      "ranges": [
        "Text"
      ]
    }, 
    "musicBy": {
      "comment": "The composer of the movie or TV soundtrack.", 
      "comment_plain": "The composer of the movie or TV soundtrack.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries"
      ], 
      "id": "musicBy", 
      "label": "Music by", 
      "ranges": [
        "Person", 
        "MusicGroup"
      ]
    }, 
    "musicGroupMember": {
      "comment": "A member of the music group\u2014for example, John, Paul, George, or Ringo.", 
      "comment_plain": "A member of the music group\u2014for example, John, Paul, George, or Ringo.", 
      "domains": [
        "MusicGroup"
      ], 
      "id": "musicGroupMember", 
      "label": "Music Group Member", 
      "ranges": [
        "Person"
      ]
    }, 
    "naics": {
      "comment": "The North American Industry Classification System (NAICS) code for a particular organization or business person.", 
      "comment_plain": "The North American Industry Classification System (NAICS) code for a particular organization or business person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "naics", 
      "label": "Naics", 
      "ranges": [
        "Text"
      ]
    }, 
    "name": {
      "comment": "The name of the item.", 
      "comment_plain": "The name of the item.", 
      "domains": [
        "Thing"
      ], 
      "id": "name", 
      "label": "Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "nationality": {
      "comment": "Nationality of the person.", 
      "comment_plain": "Nationality of the person.", 
      "domains": [
        "Person"
      ], 
      "id": "nationality", 
      "label": "Nationality", 
      "ranges": [
        "Country"
      ]
    }, 
    "naturalProgression": {
      "comment": "The expected progression of the condition if it is not treated and allowed to progress naturally.", 
      "comment_plain": "The expected progression of the condition if it is not treated and allowed to progress naturally.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "naturalProgression", 
      "label": "Natural Progression", 
      "ranges": [
        "Text"
      ]
    }, 
    "nerve": {
      "comment": "The underlying innervation associated with the muscle.", 
      "comment_plain": "The underlying innervation associated with the muscle.", 
      "domains": [
        "Muscle"
      ], 
      "id": "nerve", 
      "label": "Nerve", 
      "ranges": [
        "Nerve"
      ]
    }, 
    "nerveMotor": {
      "comment": "The neurological pathway extension that involves muscle control.", 
      "comment_plain": "The neurological pathway extension that involves muscle control.", 
      "domains": [
        "Nerve"
      ], 
      "id": "nerveMotor", 
      "label": "Nerve Motor", 
      "ranges": [
        "Muscle"
      ]
    }, 
    "nonEqual": {
      "comment": "This ordering relation for qualitative values indicates that the subject is not equal to the object.", 
      "comment_plain": "This ordering relation for qualitative values indicates that the subject is not equal to the object.", 
      "domains": [
        "QualitativeValue"
      ], 
      "id": "nonEqual", 
      "label": "Non Equal", 
      "ranges": [
        "QualitativeValue"
      ]
    }, 
    "nonProprietaryName": {
      "comment": "The generic name of this drug or supplement.", 
      "comment_plain": "The generic name of this drug or supplement.", 
      "domains": [
        "DietarySupplement", 
        "Drug"
      ], 
      "id": "nonProprietaryName", 
      "label": "Non Proprietary Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "normalRange": {
      "comment": "Range of acceptable values for a typical patient, when applicable.", 
      "comment_plain": "Range of acceptable values for a typical patient, when applicable.", 
      "domains": [
        "MedicalTest"
      ], 
      "id": "normalRange", 
      "label": "Normal Range", 
      "ranges": [
        "Text"
      ]
    }, 
    "numTracks": {
      "comment": "The number of tracks in this album or playlist.", 
      "comment_plain": "The number of tracks in this album or playlist.", 
      "domains": [
        "MusicPlaylist"
      ], 
      "id": "numTracks", 
      "label": "Num Tracks", 
      "ranges": [
        "Integer"
      ]
    }, 
    "numberOfEpisodes": {
      "comment": "The number of episodes in this season or series.", 
      "comment_plain": "The number of episodes in this season or series.", 
      "domains": [
        "TVSeason", 
        "TVSeries"
      ], 
      "id": "numberOfEpisodes", 
      "label": "Number of Episodes", 
      "ranges": [
        "Number"
      ]
    }, 
    "numberOfPages": {
      "comment": "The number of pages in the book.", 
      "comment_plain": "The number of pages in the book.", 
      "domains": [
        "Book"
      ], 
      "id": "numberOfPages", 
      "label": "Number of Pages", 
      "ranges": [
        "Integer"
      ]
    }, 
    "nutrition": {
      "comment": "Nutrition information about the recipe.", 
      "comment_plain": "Nutrition information about the recipe.", 
      "domains": [
        "Recipe"
      ], 
      "id": "nutrition", 
      "label": "Nutrition", 
      "ranges": [
        "NutritionInformation"
      ]
    }, 
    "occupationalCategory": {
      "comment": "Category or categories describing the job. Use BLS O*NET-SOC taxonomy: http://www.onetcenter.org/taxonomy.html. Ideally includes textual label and formal code, with the property repeated for each applicable value.", 
      "comment_plain": "Category or categories describing the job. Use BLS O*NET-SOC taxonomy: http://www.onetcenter.org/taxonomy.html. Ideally includes textual label and formal code, with the property repeated for each applicable value.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "occupationalCategory", 
      "label": "Occupational Category", 
      "ranges": [
        "Text"
      ]
    }, 
    "offerCount": {
      "comment": "The number of offers for the product.", 
      "comment_plain": "The number of offers for the product.", 
      "domains": [
        "AggregateOffer"
      ], 
      "id": "offerCount", 
      "label": "Offer Count", 
      "ranges": [
        "Integer"
      ]
    }, 
    "offers": {
      "comment": "An offer to sell this item\u2014for example, an offer to sell a product, the DVD of a movie, or tickets to an event.", 
      "comment_plain": "An offer to sell this item\u2014for example, an offer to sell a product, the DVD of a movie, or tickets to an event.", 
      "domains": [
        "Product", 
        "CreativeWork", 
        "Event"
      ], 
      "id": "offers", 
      "label": "Offers", 
      "ranges": [
        "Offer"
      ]
    }, 
    "openingHours": {
      "comment": "The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.<br/>- Days are specified using the following two-letter combinations: <code>Mo</code>, <code>Tu</code>, <code>We</code>, <code>Th</code>, <code>Fr</code>, <code>Sa</code>, <code>Su</code>.<br/>- Times are specified using 24:00 time. For example, 3pm is specified as <code>15:00</code>. <br/>- Here is an example: <code>&lt;time itemprop=\"openingHours\" datetime=\"Tu,Th 16:00-20:00\"&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>. <br/>- If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=\"openingHours\" datetime=\"Mo-Su\"&gt;Monday through Sunday, all day&lt;/time&gt;</code>.", 
      "comment_plain": "The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.- Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.- Times are specified using 24:00 time. For example, 3pm is specified as 15:00. - Here is an example: <time itemprop=\"openingHours\" datetime=\"Tu,Th 16:00-20:00\">Tuesdays and Thursdays 4-8pm</time>. - If a business is open 7 days a week, then it can be specified as <time itemprop=\"openingHours\" datetime=\"Mo-Su\">Monday through Sunday, all day</time>.", 
      "domains": [
        "LocalBusiness", 
        "CivicStructure"
      ], 
      "id": "openingHours", 
      "label": "Opening Hours", 
      "ranges": [
        "Duration"
      ]
    }, 
    "openingHoursSpecification": {
      "comment": "The opening hours of a certain place.", 
      "comment_plain": "The opening hours of a certain place.", 
      "domains": [
        "Place"
      ], 
      "id": "openingHoursSpecification", 
      "label": "Opening Hours Specification", 
      "ranges": [
        "OpeningHoursSpecification"
      ]
    }, 
    "opens": {
      "comment": "The opening hour of the place or service on the given day(s) of the week.", 
      "comment_plain": "The opening hour of the place or service on the given day(s) of the week.", 
      "domains": [
        "OpeningHoursSpecification"
      ], 
      "id": "opens", 
      "label": "Opens", 
      "ranges": [
        "Time"
      ]
    }, 
    "operatingSystem": {
      "comment": "Operating systems supported (Windows 7, OSX 10.6, Android 1.6).", 
      "comment_plain": "Operating systems supported (Windows 7, OSX 10.6, Android 1.6).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "operatingSystem", 
      "label": "Operating System", 
      "ranges": [
        "Text"
      ]
    }, 
    "origin": {
      "comment": "The place or point where a muscle arises.", 
      "comment_plain": "The place or point where a muscle arises.", 
      "domains": [
        "Muscle"
      ], 
      "id": "origin", 
      "label": "Origin", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "originatesFrom": {
      "comment": "The vasculature the lymphatic structure originates, or afferents, from.", 
      "comment_plain": "The vasculature the lymphatic structure originates, or afferents, from.", 
      "domains": [
        "LymphaticVessel"
      ], 
      "id": "originatesFrom", 
      "label": "Originates From", 
      "ranges": [
        "Vessel"
      ]
    }, 
    "outcome": {
      "comment": "Expected or actual outcomes of the study.", 
      "comment_plain": "Expected or actual outcomes of the study.", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "outcome", 
      "label": "Outcome", 
      "ranges": [
        "Text"
      ]
    }, 
    "overdosage": {
      "comment": "Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.", 
      "comment_plain": "Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.", 
      "domains": [
        "Drug"
      ], 
      "id": "overdosage", 
      "label": "Overdosage", 
      "ranges": [
        "Text"
      ]
    }, 
    "overview": {
      "comment": "Descriptive information establishing the overarching theory/philosophy of the plan. May include the rationale for the name, the population where the plan first came to prominence, etc.", 
      "comment_plain": "Descriptive information establishing the overarching theory/philosophy of the plan. May include the rationale for the name, the population where the plan first came to prominence, etc.", 
      "domains": [
        "Diet"
      ], 
      "id": "overview", 
      "label": "Overview", 
      "ranges": [
        "Text"
      ]
    }, 
    "ownedFrom": {
      "comment": "The date and time of obtaining the product.", 
      "comment_plain": "The date and time of obtaining the product.", 
      "domains": [
        "OwnershipInfo"
      ], 
      "id": "ownedFrom", 
      "label": "Owned From", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "ownedThrough": {
      "comment": "The date and time of giving up ownership on the product.", 
      "comment_plain": "The date and time of giving up ownership on the product.", 
      "domains": [
        "OwnershipInfo"
      ], 
      "id": "ownedThrough", 
      "label": "Owned Through", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "owns": {
      "comment": "Products owned by the organization or person.", 
      "comment_plain": "Products owned by the organization or person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "owns", 
      "label": "Owns", 
      "ranges": [
        "OwnershipInfo", 
        "Product"
      ]
    }, 
    "parent": {
      "comment": "A parent of this person.", 
      "comment_plain": "A parent of this person.", 
      "domains": [
        "Person"
      ], 
      "id": "parent", 
      "label": "Parent", 
      "ranges": [
        "Person"
      ]
    }, 
    "parents": {
      "comment": "A parents of the person (legacy spelling; see singular form, parent).", 
      "comment_plain": "A parents of the person (legacy spelling; see singular form, parent).", 
      "domains": [
        "Person"
      ], 
      "id": "parents", 
      "label": "Parents", 
      "ranges": [
        "Person"
      ]
    }, 
    "partOfSeason": {
      "comment": "The season to which this episode belongs.", 
      "comment_plain": "The season to which this episode belongs.", 
      "domains": [
        "TVEpisode"
      ], 
      "id": "partOfSeason", 
      "label": "Part of Season", 
      "ranges": [
        "TVSeason"
      ]
    }, 
    "partOfSystem": {
      "comment": "The anatomical or organ system that this structure is part of.", 
      "comment_plain": "The anatomical or organ system that this structure is part of.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "partOfSystem", 
      "label": "Part of System", 
      "ranges": [
        "AnatomicalSystem"
      ]
    }, 
    "partOfTVSeries": {
      "comment": "The TV series to which this episode or season belongs.", 
      "comment_plain": "The TV series to which this episode or season belongs.", 
      "domains": [
        "TVEpisode", 
        "TVSeason"
      ], 
      "id": "partOfTVSeries", 
      "label": "Part of TV Series", 
      "ranges": [
        "TVSeries"
      ]
    }, 
    "pathophysiology": {
      "comment": "Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.", 
      "comment_plain": "Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.", 
      "domains": [
        "MedicalCondition", 
        "PhysicalActivity"
      ], 
      "id": "pathophysiology", 
      "label": "Pathophysiology", 
      "ranges": [
        "Text"
      ]
    }, 
    "paymentAccepted": {
      "comment": "Cash, credit card, etc.", 
      "comment_plain": "Cash, credit card, etc.", 
      "domains": [
        "LocalBusiness"
      ], 
      "id": "paymentAccepted", 
      "label": "Payment Accepted", 
      "ranges": [
        "Text"
      ]
    }, 
    "performer": {
      "comment": "A performer at the event\u2014for example, a presenter, musician, musical group or actor.", 
      "comment_plain": "A performer at the event\u2014for example, a presenter, musician, musical group or actor.", 
      "domains": [
        "Event"
      ], 
      "id": "performer", 
      "label": "Performer", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "performerIn": {
      "comment": "Event that this person is a performer or participant in.", 
      "comment_plain": "Event that this person is a performer or participant in.", 
      "domains": [
        "Person"
      ], 
      "id": "performerIn", 
      "label": "Performer in", 
      "ranges": [
        "Event"
      ]
    }, 
    "performers": {
      "comment": "The main performer or performers of the event\u2014for example, a presenter, musician, or actor (legacy spelling; see singular form, performer).", 
      "comment_plain": "The main performer or performers of the event\u2014for example, a presenter, musician, or actor (legacy spelling; see singular form, performer).", 
      "domains": [
        "Event"
      ], 
      "id": "performers", 
      "label": "Performers", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "permissions": {
      "comment": "Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).", 
      "comment_plain": "Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "permissions", 
      "label": "Permissions", 
      "ranges": [
        "Text"
      ]
    }, 
    "phase": {
      "comment": "The phase of the trial.", 
      "comment_plain": "The phase of the trial.", 
      "domains": [
        "MedicalTrial"
      ], 
      "id": "phase", 
      "label": "Phase", 
      "ranges": [
        "Text"
      ]
    }, 
    "photo": {
      "comment": "A photograph of this place.", 
      "comment_plain": "A photograph of this place.", 
      "domains": [
        "Place"
      ], 
      "id": "photo", 
      "label": "Photo", 
      "ranges": [
        "ImageObject", 
        "Photograph"
      ]
    }, 
    "photos": {
      "comment": "Photographs of this place (legacy spelling; see singular form, photo).", 
      "comment_plain": "Photographs of this place (legacy spelling; see singular form, photo).", 
      "domains": [
        "Place"
      ], 
      "id": "photos", 
      "label": "Photos", 
      "ranges": [
        "ImageObject", 
        "Photograph"
      ]
    }, 
    "physiologicalBenefits": {
      "comment": "Specific physiologic benefits associated to the plan.", 
      "comment_plain": "Specific physiologic benefits associated to the plan.", 
      "domains": [
        "Diet"
      ], 
      "id": "physiologicalBenefits", 
      "label": "Physiological Benefits", 
      "ranges": [
        "Text"
      ]
    }, 
    "playerType": {
      "comment": "Player type required\u2014for example, Flash or Silverlight.", 
      "comment_plain": "Player type required\u2014for example, Flash or Silverlight.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "playerType", 
      "label": "Player Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "polygon": {
      "comment": "A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more spacedelimited points where the first and final points are identical.", 
      "comment_plain": "A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more spacedelimited points where the first and final points are identical.", 
      "domains": [
        "GeoShape"
      ], 
      "id": "polygon", 
      "label": "Polygon", 
      "ranges": [
        "Text"
      ]
    }, 
    "population": {
      "comment": "Any characteristics of the population used in the study, e.g. 'males under 65'.", 
      "comment_plain": "Any characteristics of the population used in the study, e.g. 'males under 65'.", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "population", 
      "label": "Population", 
      "ranges": [
        "Text"
      ]
    }, 
    "possibleComplication": {
      "comment": "A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.", 
      "comment_plain": "A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "possibleComplication", 
      "label": "Possible Complication", 
      "ranges": [
        "Text"
      ]
    }, 
    "possibleTreatment": {
      "comment": "A possible treatment to address this condition, sign or symptom.", 
      "comment_plain": "A possible treatment to address this condition, sign or symptom.", 
      "domains": [
        "MedicalCondition", 
        "MedicalSignOrSymptom"
      ], 
      "id": "possibleTreatment", 
      "label": "Possible Treatment", 
      "ranges": [
        "MedicalTherapy"
      ]
    }, 
    "postOfficeBoxNumber": {
      "comment": "The post offce box number for PO box addresses.", 
      "comment_plain": "The post offce box number for PO box addresses.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "postOfficeBoxNumber", 
      "label": "Post Office Box Number", 
      "ranges": [
        "Text"
      ]
    }, 
    "postOp": {
      "comment": "A description of the postoperative procedures, care, and/or followups for this device.", 
      "comment_plain": "A description of the postoperative procedures, care, and/or followups for this device.", 
      "domains": [
        "MedicalDevice"
      ], 
      "id": "postOp", 
      "label": "Post Op", 
      "ranges": [
        "Text"
      ]
    }, 
    "postalCode": {
      "comment": "The postal code. For example, 94043.", 
      "comment_plain": "The postal code. For example, 94043.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "postalCode", 
      "label": "Postal Code", 
      "ranges": [
        "Text"
      ]
    }, 
    "preOp": {
      "comment": "A description of the workup, testing, and other preparations required before implanting this device.", 
      "comment_plain": "A description of the workup, testing, and other preparations required before implanting this device.", 
      "domains": [
        "MedicalDevice"
      ], 
      "id": "preOp", 
      "label": "Pre Op", 
      "ranges": [
        "Text"
      ]
    }, 
    "predecessorOf": {
      "comment": "A pointer from a previous, often discontinued variant of the product to its newer variant.", 
      "comment_plain": "A pointer from a previous, often discontinued variant of the product to its newer variant.", 
      "domains": [
        "ProductModel"
      ], 
      "id": "predecessorOf", 
      "label": "Predecessor of", 
      "ranges": [
        "ProductModel"
      ]
    }, 
    "pregnancyCategory": {
      "comment": "Pregnancy category of this drug.", 
      "comment_plain": "Pregnancy category of this drug.", 
      "domains": [
        "Drug"
      ], 
      "id": "pregnancyCategory", 
      "label": "Pregnancy Category", 
      "ranges": [
        "DrugPregnancyCategory"
      ]
    }, 
    "pregnancyWarning": {
      "comment": "Any precaution, guidance, contraindication, etc. related to this drug's use during pregnancy.", 
      "comment_plain": "Any precaution, guidance, contraindication, etc. related to this drug's use during pregnancy.", 
      "domains": [
        "Drug"
      ], 
      "id": "pregnancyWarning", 
      "label": "Pregnancy Warning", 
      "ranges": [
        "Text"
      ]
    }, 
    "prepTime": {
      "comment": "The length of time it takes to prepare the recipe, in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 duration format</a>.", 
      "comment_plain": "The length of time it takes to prepare the recipe, in ISO 8601 duration format.", 
      "domains": [
        "Recipe"
      ], 
      "id": "prepTime", 
      "label": "Prep Time", 
      "ranges": [
        "Duration"
      ]
    }, 
    "preparation": {
      "comment": "Typical preparation that a patient must undergo before having the procedure performed.", 
      "comment_plain": "Typical preparation that a patient must undergo before having the procedure performed.", 
      "domains": [
        "MedicalProcedure"
      ], 
      "id": "preparation", 
      "label": "Preparation", 
      "ranges": [
        "Text"
      ]
    }, 
    "prescribingInfo": {
      "comment": "Link to prescribing information for the drug.", 
      "comment_plain": "Link to prescribing information for the drug.", 
      "domains": [
        "Drug"
      ], 
      "id": "prescribingInfo", 
      "label": "Prescribing Info", 
      "ranges": [
        "URL"
      ]
    }, 
    "prescriptionStatus": {
      "comment": "Indicates whether this drug is available by prescription or over-the-counter.", 
      "comment_plain": "Indicates whether this drug is available by prescription or over-the-counter.", 
      "domains": [
        "Drug"
      ], 
      "id": "prescriptionStatus", 
      "label": "Prescription Status", 
      "ranges": [
        "DrugPrescriptionStatus"
      ]
    }, 
    "price": {
      "comment": "The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.", 
      "comment_plain": "The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.", 
      "domains": [
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "price", 
      "label": "Price", 
      "ranges": [
        "Text", 
        "Number"
      ]
    }, 
    "priceCurrency": {
      "comment": "The currency (in 3-letter ISO 4217 format) of the offer price or a price component, when attached to PriceSpecification and its subtypes.", 
      "comment_plain": "The currency (in 3-letter ISO 4217 format) of the offer price or a price component, when attached to PriceSpecification and its subtypes.", 
      "domains": [
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "priceCurrency", 
      "label": "Price Currency", 
      "ranges": [
        "Text"
      ]
    }, 
    "priceRange": {
      "comment": "The price range of the business, for example <code>$$$</code>.", 
      "comment_plain": "The price range of the business, for example $$$.", 
      "domains": [
        "LocalBusiness"
      ], 
      "id": "priceRange", 
      "label": "Price Range", 
      "ranges": [
        "Text"
      ]
    }, 
    "priceSpecification": {
      "comment": "One or more detailed price specifications, indicating the unit price and delivery or payment charges.", 
      "comment_plain": "One or more detailed price specifications, indicating the unit price and delivery or payment charges.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "priceSpecification", 
      "label": "Price Specification", 
      "ranges": [
        "PriceSpecification"
      ]
    }, 
    "priceType": {
      "comment": "A short text or acronym indicating multiple price specifications for the same offer, e.g. SRP for the suggested retail price or INVOICE for the invoice price, mostly used in the car industry.", 
      "comment_plain": "A short text or acronym indicating multiple price specifications for the same offer, e.g. SRP for the suggested retail price or INVOICE for the invoice price, mostly used in the car industry.", 
      "domains": [
        "UnitPriceSpecification"
      ], 
      "id": "priceType", 
      "label": "Price Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "priceValidUntil": {
      "comment": "The date after which the price is no longer available.", 
      "comment_plain": "The date after which the price is no longer available.", 
      "domains": [
        "Offer"
      ], 
      "id": "priceValidUntil", 
      "label": "Price Valid Until", 
      "ranges": [
        "Date"
      ]
    }, 
    "primaryImageOfPage": {
      "comment": "Indicates the main image on the page", 
      "comment_plain": "Indicates the main image on the page", 
      "domains": [
        "WebPage"
      ], 
      "id": "primaryImageOfPage", 
      "label": "Primary Image of Page", 
      "ranges": [
        "ImageObject"
      ]
    }, 
    "primaryPrevention": {
      "comment": "A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.", 
      "comment_plain": "A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "primaryPrevention", 
      "label": "Primary Prevention", 
      "ranges": [
        "MedicalTherapy"
      ]
    }, 
    "printColumn": {
      "comment": "The number of the column in which the NewsArticle appears in the print edition.", 
      "comment_plain": "The number of the column in which the NewsArticle appears in the print edition.", 
      "domains": [
        "NewsArticle"
      ], 
      "id": "printColumn", 
      "label": "Print Column", 
      "ranges": [
        "Text"
      ]
    }, 
    "printEdition": {
      "comment": "The edition of the print product in which the NewsArticle appears.", 
      "comment_plain": "The edition of the print product in which the NewsArticle appears.", 
      "domains": [
        "NewsArticle"
      ], 
      "id": "printEdition", 
      "label": "Print Edition", 
      "ranges": [
        "Text"
      ]
    }, 
    "printPage": {
      "comment": "If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).", 
      "comment_plain": "If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).", 
      "domains": [
        "NewsArticle"
      ], 
      "id": "printPage", 
      "label": "Print Page", 
      "ranges": [
        "Text"
      ]
    }, 
    "printSection": {
      "comment": "If this NewsArticle appears in print, this field indicates the print section in which the article appeared.", 
      "comment_plain": "If this NewsArticle appears in print, this field indicates the print section in which the article appeared.", 
      "domains": [
        "NewsArticle"
      ], 
      "id": "printSection", 
      "label": "Print Section", 
      "ranges": [
        "Text"
      ]
    }, 
    "procedure": {
      "comment": "A description of the procedure involved in setting up, using, and/or installing the device.", 
      "comment_plain": "A description of the procedure involved in setting up, using, and/or installing the device.", 
      "domains": [
        "MedicalDevice"
      ], 
      "id": "procedure", 
      "label": "Procedure", 
      "ranges": [
        "Text"
      ]
    }, 
    "procedureType": {
      "comment": "The type of procedure, for example Surgical, Noninvasive, or Percutaneous.", 
      "comment_plain": "The type of procedure, for example Surgical, Noninvasive, or Percutaneous.", 
      "domains": [
        "MedicalProcedure"
      ], 
      "id": "procedureType", 
      "label": "Procedure Type", 
      "ranges": [
        "MedicalProcedureType"
      ]
    }, 
    "processorRequirements": {
      "comment": "Processor architecture required to run the application (e.g. IA64).", 
      "comment_plain": "Processor architecture required to run the application (e.g. IA64).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "processorRequirements", 
      "label": "Processor Requirements", 
      "ranges": [
        "Text"
      ]
    }, 
    "producer": {
      "comment": "The producer of the movie, TV series, season, or episode, or video.", 
      "comment_plain": "The producer of the movie, TV series, season, or episode, or video.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries"
      ], 
      "id": "producer", 
      "label": "Producer", 
      "ranges": [
        "Person"
      ]
    }, 
    "productID": {
      "comment": "The product identifier, such as ISBN. For example: <code>&lt;meta itemprop='productID' content='isbn:123-456-789'/&gt;</code>.", 
      "comment_plain": "The product identifier, such as ISBN. For example: <meta itemprop='productID' content='isbn:123-456-789'/>.", 
      "domains": [
        "Product"
      ], 
      "id": "productID", 
      "label": "Product ID", 
      "ranges": [
        "Text"
      ]
    }, 
    "productionCompany": {
      "comment": "The production company or studio that made the movie, TV series, season, or episode, or video.", 
      "comment_plain": "The production company or studio that made the movie, TV series, season, or episode, or video.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "VideoObject", 
        "TVSeries"
      ], 
      "id": "productionCompany", 
      "label": "Production Company", 
      "ranges": [
        "Organization"
      ]
    }, 
    "proficiencyLevel": {
      "comment": "Proficiency needed for this content; expected values: 'Beginner', 'Expert'.", 
      "comment_plain": "Proficiency needed for this content; expected values: 'Beginner', 'Expert'.", 
      "domains": [
        "TechArticle"
      ], 
      "id": "proficiencyLevel", 
      "label": "Proficiency Level", 
      "ranges": [
        "Text"
      ]
    }, 
    "programmingLanguage": {
      "comment": "The computer programming language.", 
      "comment_plain": "The computer programming language.", 
      "domains": [
        "Code"
      ], 
      "id": "programmingLanguage", 
      "label": "Programming Language", 
      "ranges": [
        "Thing"
      ]
    }, 
    "programmingModel": {
      "comment": "Indicates whether API is managed or unmanaged.", 
      "comment_plain": "Indicates whether API is managed or unmanaged.", 
      "domains": [
        "APIReference"
      ], 
      "id": "programmingModel", 
      "label": "Programming Model", 
      "ranges": [
        "Text"
      ]
    }, 
    "proprietaryName": {
      "comment": "Proprietary name given to the diet plan, typically by its originator or creator.", 
      "comment_plain": "Proprietary name given to the diet plan, typically by its originator or creator.", 
      "domains": [
        "Diet"
      ], 
      "id": "proprietaryName", 
      "label": "Proprietary Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "proteinContent": {
      "comment": "The number of grams of protein.", 
      "comment_plain": "The number of grams of protein.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "proteinContent", 
      "label": "Protein Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "provider": {
      "comment": "Specifies the Person or Organization that distributed the CreativeWork.", 
      "comment_plain": "Specifies the Person or Organization that distributed the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "provider", 
      "label": "Provider", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "publicationType": {
      "comment": "The type of the medical article, taken from the US NLM MeSH <a href=\"http://www.nlm.nih.gov/mesh/pubtypes.html\">publication type catalog.</a>", 
      "comment_plain": "The type of the medical article, taken from the US NLM MeSH publication type catalog.", 
      "domains": [
        "MedicalScholarlyArticle"
      ], 
      "id": "publicationType", 
      "label": "Publication Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "publisher": {
      "comment": "The publisher of the creative work.", 
      "comment_plain": "The publisher of the creative work.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "publisher", 
      "label": "Publisher", 
      "ranges": [
        "Organization"
      ]
    }, 
    "publishingPrinciples": {
      "comment": "Link to page describing the editorial principles of the organization primarily responsible for the creation of the CreativeWork.", 
      "comment_plain": "Link to page describing the editorial principles of the organization primarily responsible for the creation of the CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "publishingPrinciples", 
      "label": "Publishing Principles", 
      "ranges": [
        "URL"
      ]
    }, 
    "purpose": {
      "comment": "The purpose or purposes of this device, for example whether it is intended for diagnostic or therapeutic use.", 
      "comment_plain": "The purpose or purposes of this device, for example whether it is intended for diagnostic or therapeutic use.", 
      "domains": [
        "MedicalDevice"
      ], 
      "id": "purpose", 
      "label": "Purpose", 
      "ranges": [
        "MedicalDevicePurpose"
      ]
    }, 
    "qualifications": {
      "comment": "Specific qualifications required for this role.", 
      "comment_plain": "Specific qualifications required for this role.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "qualifications", 
      "label": "Qualifications", 
      "ranges": [
        "Text"
      ]
    }, 
    "rangeIncludes": {
      "comment": "Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.", 
      "comment_plain": "Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.", 
      "domains": [
        "Property"
      ], 
      "id": "rangeIncludes", 
      "label": "Range Includes", 
      "ranges": [
        "Class"
      ]
    }, 
    "ratingCount": {
      "comment": "The count of total number of ratings.", 
      "comment_plain": "The count of total number of ratings.", 
      "domains": [
        "AggregateRating"
      ], 
      "id": "ratingCount", 
      "label": "Rating Count", 
      "ranges": [
        "Number"
      ]
    }, 
    "ratingValue": {
      "comment": "The rating for the content.", 
      "comment_plain": "The rating for the content.", 
      "domains": [
        "Rating"
      ], 
      "id": "ratingValue", 
      "label": "Rating Value", 
      "ranges": [
        "Text"
      ]
    }, 
    "recipeCategory": {
      "comment": "The category of the recipe\u2014for example, appetizer, entree, etc.", 
      "comment_plain": "The category of the recipe\u2014for example, appetizer, entree, etc.", 
      "domains": [
        "Recipe"
      ], 
      "id": "recipeCategory", 
      "label": "Recipe Category", 
      "ranges": [
        "Text"
      ]
    }, 
    "recipeCuisine": {
      "comment": "The cuisine of the recipe (for example, French or Ethopian).", 
      "comment_plain": "The cuisine of the recipe (for example, French or Ethopian).", 
      "domains": [
        "Recipe"
      ], 
      "id": "recipeCuisine", 
      "label": "Recipe Cuisine", 
      "ranges": [
        "Text"
      ]
    }, 
    "recipeInstructions": {
      "comment": "The steps to make the dish.", 
      "comment_plain": "The steps to make the dish.", 
      "domains": [
        "Recipe"
      ], 
      "id": "recipeInstructions", 
      "label": "Recipe Instructions", 
      "ranges": [
        "Text"
      ]
    }, 
    "recipeYield": {
      "comment": "The quantity produced by the recipe (for example, number of people served, number of servings, etc).", 
      "comment_plain": "The quantity produced by the recipe (for example, number of people served, number of servings, etc).", 
      "domains": [
        "Recipe"
      ], 
      "id": "recipeYield", 
      "label": "Recipe Yield", 
      "ranges": [
        "Text"
      ]
    }, 
    "recognizingAuthority": {
      "comment": "If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.", 
      "comment_plain": "If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "recognizingAuthority", 
      "label": "Recognizing Authority", 
      "ranges": [
        "Organization"
      ]
    }, 
    "recommendationStrength": {
      "comment": "Strength of the guideline's recommendation (e.g. 'class I').", 
      "comment_plain": "Strength of the guideline's recommendation (e.g. 'class I').", 
      "domains": [
        "MedicalGuidelineRecommendation"
      ], 
      "id": "recommendationStrength", 
      "label": "Recommendation Strength", 
      "ranges": [
        "Text"
      ]
    }, 
    "recommendedIntake": {
      "comment": "Recommended intake of this supplement for a given population as defined by a specific recommending authority.", 
      "comment_plain": "Recommended intake of this supplement for a given population as defined by a specific recommending authority.", 
      "domains": [
        "DietarySupplement"
      ], 
      "id": "recommendedIntake", 
      "label": "Recommended Intake", 
      "ranges": [
        "RecommendedDoseSchedule"
      ]
    }, 
    "regionDrained": {
      "comment": "The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.", 
      "comment_plain": "The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.", 
      "domains": [
        "LymphaticVessel", 
        "Vein"
      ], 
      "id": "regionDrained", 
      "label": "Region Drained", 
      "ranges": [
        "AnatomicalSystem", 
        "AnatomicalStructure"
      ]
    }, 
    "regionsAllowed": {
      "comment": "The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in <a href=\"http://en.wikipedia.org/wiki/ISO_3166\">ISO 3166 format</a>.", 
      "comment_plain": "The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in ISO 3166 format.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "regionsAllowed", 
      "label": "Regions Allowed", 
      "ranges": [
        "Place"
      ]
    }, 
    "relatedAnatomy": {
      "comment": "Anatomical systems or structures that relate to the superficial anatomy.", 
      "comment_plain": "Anatomical systems or structures that relate to the superficial anatomy.", 
      "domains": [
        "SuperficialAnatomy"
      ], 
      "id": "relatedAnatomy", 
      "label": "Related Anatomy", 
      "ranges": [
        "AnatomicalStructure", 
        "AnatomicalSystem"
      ]
    }, 
    "relatedCondition": {
      "comment": "A medical condition associated with this anatomy.", 
      "comment_plain": "A medical condition associated with this anatomy.", 
      "domains": [
        "SuperficialAnatomy", 
        "AnatomicalSystem", 
        "AnatomicalStructure"
      ], 
      "id": "relatedCondition", 
      "label": "Related Condition", 
      "ranges": [
        "MedicalCondition"
      ]
    }, 
    "relatedDrug": {
      "comment": "Any other drug related to this one, for example commonly-prescribed alternatives.", 
      "comment_plain": "Any other drug related to this one, for example commonly-prescribed alternatives.", 
      "domains": [
        "Drug"
      ], 
      "id": "relatedDrug", 
      "label": "Related Drug", 
      "ranges": [
        "Drug"
      ]
    }, 
    "relatedLink": {
      "comment": "A link related to this web page, for example to other related web pages.", 
      "comment_plain": "A link related to this web page, for example to other related web pages.", 
      "domains": [
        "WebPage"
      ], 
      "id": "relatedLink", 
      "label": "Related Link", 
      "ranges": [
        "URL"
      ]
    }, 
    "relatedStructure": {
      "comment": "Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.", 
      "comment_plain": "Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.", 
      "domains": [
        "AnatomicalSystem"
      ], 
      "id": "relatedStructure", 
      "label": "Related Structure", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "relatedTherapy": {
      "comment": "A medical therapy related to this anatomy.", 
      "comment_plain": "A medical therapy related to this anatomy.", 
      "domains": [
        "SuperficialAnatomy", 
        "AnatomicalSystem", 
        "AnatomicalStructure"
      ], 
      "id": "relatedTherapy", 
      "label": "Related Therapy", 
      "ranges": [
        "MedicalTherapy"
      ]
    }, 
    "relatedTo": {
      "comment": "The most generic familial relation.", 
      "comment_plain": "The most generic familial relation.", 
      "domains": [
        "Person"
      ], 
      "id": "relatedTo", 
      "label": "Related to", 
      "ranges": [
        "Person"
      ]
    }, 
    "releaseDate": {
      "comment": "The release date of a product or product model. This can be used to distinguish the exact variant of a product.", 
      "comment_plain": "The release date of a product or product model. This can be used to distinguish the exact variant of a product.", 
      "domains": [
        "Product"
      ], 
      "id": "releaseDate", 
      "label": "Release Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "releaseNotes": {
      "comment": "Description of what changed in this version.", 
      "comment_plain": "Description of what changed in this version.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "releaseNotes", 
      "label": "Release Notes", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "relevantSpecialty": {
      "comment": "If applicable, a medical specialty in which this entity is relevant.", 
      "comment_plain": "If applicable, a medical specialty in which this entity is relevant.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "relevantSpecialty", 
      "label": "Relevant Specialty", 
      "ranges": [
        "MedicalSpecialty"
      ]
    }, 
    "repetitions": {
      "comment": "Number of times one should repeat the activity.", 
      "comment_plain": "Number of times one should repeat the activity.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "repetitions", 
      "label": "Repetitions", 
      "ranges": [
        "Number"
      ]
    }, 
    "replyToUrl": {
      "comment": "The URL at which a reply may be posted to the specified UserComment.", 
      "comment_plain": "The URL at which a reply may be posted to the specified UserComment.", 
      "domains": [
        "UserComments"
      ], 
      "id": "replyToUrl", 
      "label": "Reply to Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "representativeOfPage": {
      "comment": "Indicates whether this image is representative of the content of the page.", 
      "comment_plain": "Indicates whether this image is representative of the content of the page.", 
      "domains": [
        "ImageObject"
      ], 
      "id": "representativeOfPage", 
      "label": "Representative of Page", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "requirements": {
      "comment": "Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).", 
      "comment_plain": "Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "requirements", 
      "label": "Requirements", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "requiresSubscription": {
      "comment": "Indicates if use of the media require a subscription  (either paid or free). Allowed values are <code>true</code> or <code>false</code> (note that an earlier version had 'yes', 'no').", 
      "comment_plain": "Indicates if use of the media require a subscription  (either paid or free). Allowed values are true or false (note that an earlier version had 'yes', 'no').", 
      "domains": [
        "MediaObject"
      ], 
      "id": "requiresSubscription", 
      "label": "Requires Subscription", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "responsibilities": {
      "comment": "Responsibilities associated with this role.", 
      "comment_plain": "Responsibilities associated with this role.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "responsibilities", 
      "label": "Responsibilities", 
      "ranges": [
        "Text"
      ]
    }, 
    "restPeriods": {
      "comment": "How often one should break from the activity.", 
      "comment_plain": "How often one should break from the activity.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "restPeriods", 
      "label": "Rest Periods", 
      "ranges": [
        "Text"
      ]
    }, 
    "review": {
      "comment": "A review of the item.", 
      "comment_plain": "A review of the item.", 
      "domains": [
        "Organization", 
        "Product", 
        "CreativeWork", 
        "Place", 
        "Offer"
      ], 
      "id": "review", 
      "label": "Review", 
      "ranges": [
        "Review"
      ]
    }, 
    "reviewBody": {
      "comment": "The actual body of the review", 
      "comment_plain": "The actual body of the review", 
      "domains": [
        "Review"
      ], 
      "id": "reviewBody", 
      "label": "Review Body", 
      "ranges": [
        "Text"
      ]
    }, 
    "reviewCount": {
      "comment": "The count of total number of reviews.", 
      "comment_plain": "The count of total number of reviews.", 
      "domains": [
        "AggregateRating"
      ], 
      "id": "reviewCount", 
      "label": "Review Count", 
      "ranges": [
        "Number"
      ]
    }, 
    "reviewRating": {
      "comment": "The rating given in this review. Note that reviews can themselves be rated. The <code>reviewRating</code> applies to rating given by the review. The <code>aggregateRating</code> property applies to the review itself, as a creative work.", 
      "comment_plain": "The rating given in this review. Note that reviews can themselves be rated. The reviewRating applies to rating given by the review. The aggregateRating property applies to the review itself, as a creative work.", 
      "domains": [
        "Review"
      ], 
      "id": "reviewRating", 
      "label": "Review Rating", 
      "ranges": [
        "Rating"
      ]
    }, 
    "reviewedBy": {
      "comment": "People or organizations that have reviewed the content on this web page for accuracy and/or completeness.", 
      "comment_plain": "People or organizations that have reviewed the content on this web page for accuracy and/or completeness.", 
      "domains": [
        "WebPage"
      ], 
      "id": "reviewedBy", 
      "label": "Reviewed by", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "reviews": {
      "comment": "Review of the item (legacy spelling; see singular form, review).", 
      "comment_plain": "Review of the item (legacy spelling; see singular form, review).", 
      "domains": [
        "Organization", 
        "Product", 
        "CreativeWork", 
        "Place", 
        "Offer"
      ], 
      "id": "reviews", 
      "label": "Reviews", 
      "ranges": [
        "Review"
      ]
    }, 
    "riskFactor": {
      "comment": "A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.", 
      "comment_plain": "A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "riskFactor", 
      "label": "Risk Factor", 
      "ranges": [
        "MedicalRiskFactor"
      ]
    }, 
    "risks": {
      "comment": "Specific physiologic risks associated to the plan.", 
      "comment_plain": "Specific physiologic risks associated to the plan.", 
      "domains": [
        "Diet"
      ], 
      "id": "risks", 
      "label": "Risks", 
      "ranges": [
        "Text"
      ]
    }, 
    "runsTo": {
      "comment": "The vasculature the lymphatic structure runs, or efferents, to.", 
      "comment_plain": "The vasculature the lymphatic structure runs, or efferents, to.", 
      "domains": [
        "LymphaticVessel"
      ], 
      "id": "runsTo", 
      "label": "Runs to", 
      "ranges": [
        "Vessel"
      ]
    }, 
    "runtime": {
      "comment": "Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0)", 
      "comment_plain": "Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0)", 
      "domains": [
        "Code"
      ], 
      "id": "runtime", 
      "label": "Runtime", 
      "ranges": [
        "Text"
      ]
    }, 
    "safetyConsideration": {
      "comment": "Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.", 
      "comment_plain": "Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.", 
      "domains": [
        "DietarySupplement"
      ], 
      "id": "safetyConsideration", 
      "label": "Safety Consideration", 
      "ranges": [
        "Text"
      ]
    }, 
    "salaryCurrency": {
      "comment": "The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 used for the main salary information in this job posting.", 
      "comment_plain": "The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 used for the main salary information in this job posting.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "salaryCurrency", 
      "label": "Salary Currency", 
      "ranges": [
        "Text"
      ]
    }, 
    "sampleType": {
      "comment": "Full (compile ready) solution, code snippet, inline code, scripts, template.", 
      "comment_plain": "Full (compile ready) solution, code snippet, inline code, scripts, template.", 
      "domains": [
        "Code"
      ], 
      "id": "sampleType", 
      "label": "Sample Type", 
      "ranges": [
        "Text"
      ]
    }, 
    "saturatedFatContent": {
      "comment": "The number of grams of saturated fat.", 
      "comment_plain": "The number of grams of saturated fat.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "saturatedFatContent", 
      "label": "Saturated Fat Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "screenshot": {
      "comment": "A link to a screenshot image of the app.", 
      "comment_plain": "A link to a screenshot image of the app.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "screenshot", 
      "label": "Screenshot", 
      "ranges": [
        "ImageObject", 
        "URL"
      ]
    }, 
    "season": {
      "comment": "A season of a TV series.", 
      "comment_plain": "A season of a TV series.", 
      "domains": [
        "TVSeries"
      ], 
      "id": "season", 
      "label": "Season", 
      "ranges": [
        "TVSeason"
      ]
    }, 
    "seasonNumber": {
      "comment": "The season number.", 
      "comment_plain": "The season number.", 
      "domains": [
        "TVSeason"
      ], 
      "id": "seasonNumber", 
      "label": "Season Number", 
      "ranges": [
        "Integer"
      ]
    }, 
    "seasons": {
      "comment": "The seasons of the TV series (legacy spelling; see singular form, season).", 
      "comment_plain": "The seasons of the TV series (legacy spelling; see singular form, season).", 
      "domains": [
        "TVSeries"
      ], 
      "id": "seasons", 
      "label": "Seasons", 
      "ranges": [
        "TVSeason"
      ]
    }, 
    "secondaryPrevention": {
      "comment": "A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.", 
      "comment_plain": "A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "secondaryPrevention", 
      "label": "Secondary Prevention", 
      "ranges": [
        "MedicalTherapy"
      ]
    }, 
    "seeks": {
      "comment": "A pointer to products or services sought by the organization or person (demand).", 
      "comment_plain": "A pointer to products or services sought by the organization or person (demand).", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "seeks", 
      "label": "Seeks", 
      "ranges": [
        "Demand"
      ]
    }, 
    "seller": {
      "comment": "The seller.", 
      "comment_plain": "The seller.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "seller", 
      "label": "Seller", 
      "ranges": [
        "Organization", 
        "Person"
      ]
    }, 
    "sensoryUnit": {
      "comment": "The neurological pathway extension that inputs and sends information to the brain or spinal cord.", 
      "comment_plain": "The neurological pathway extension that inputs and sends information to the brain or spinal cord.", 
      "domains": [
        "Nerve"
      ], 
      "id": "sensoryUnit", 
      "label": "Sensory Unit", 
      "ranges": [
        "AnatomicalStructure", 
        "SuperficialAnatomy"
      ]
    }, 
    "serialNumber": {
      "comment": "The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.", 
      "comment_plain": "The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.", 
      "domains": [
        "Demand", 
        "IndividualProduct", 
        "Offer"
      ], 
      "id": "serialNumber", 
      "label": "Serial Number", 
      "ranges": [
        "Text"
      ]
    }, 
    "seriousAdverseOutcome": {
      "comment": "A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.", 
      "comment_plain": "A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.", 
      "domains": [
        "MedicalDevice", 
        "MedicalTherapy"
      ], 
      "id": "seriousAdverseOutcome", 
      "label": "Serious Adverse Outcome", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "servesCuisine": {
      "comment": "The cuisine of the restaurant.", 
      "comment_plain": "The cuisine of the restaurant.", 
      "domains": [
        "FoodEstablishment"
      ], 
      "id": "servesCuisine", 
      "label": "Serves Cuisine", 
      "ranges": [
        "Text"
      ]
    }, 
    "servingSize": {
      "comment": "The serving size, in terms of the number of volume or mass", 
      "comment_plain": "The serving size, in terms of the number of volume or mass", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "servingSize", 
      "label": "Serving Size", 
      "ranges": [
        "Text"
      ]
    }, 
    "sibling": {
      "comment": "A sibling of the person.", 
      "comment_plain": "A sibling of the person.", 
      "domains": [
        "Person"
      ], 
      "id": "sibling", 
      "label": "Sibling", 
      "ranges": [
        "Person"
      ]
    }, 
    "siblings": {
      "comment": "A sibling of the person (legacy spelling; see singular form, sibling).", 
      "comment_plain": "A sibling of the person (legacy spelling; see singular form, sibling).", 
      "domains": [
        "Person"
      ], 
      "id": "siblings", 
      "label": "Siblings", 
      "ranges": [
        "Person"
      ]
    }, 
    "signDetected": {
      "comment": "A sign detected by the test.", 
      "comment_plain": "A sign detected by the test.", 
      "domains": [
        "MedicalTest"
      ], 
      "id": "signDetected", 
      "label": "Sign Detected", 
      "ranges": [
        "MedicalSign"
      ]
    }, 
    "signOrSymptom": {
      "comment": "A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experienceof the medical condition.", 
      "comment_plain": "A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experienceof the medical condition.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "signOrSymptom", 
      "label": "Sign or Symptom", 
      "ranges": [
        "MedicalSignOrSymptom"
      ]
    }, 
    "significance": {
      "comment": "The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.", 
      "comment_plain": "The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.", 
      "domains": [
        "SuperficialAnatomy"
      ], 
      "id": "significance", 
      "label": "Significance", 
      "ranges": [
        "Text"
      ]
    }, 
    "significantLink": {
      "comment": "One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.", 
      "comment_plain": "One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.", 
      "domains": [
        "WebPage"
      ], 
      "id": "significantLink", 
      "label": "Significant Link", 
      "ranges": [
        "URL"
      ]
    }, 
    "significantLinks": {
      "comment": "The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most (legacy spelling; see singular form, significantLink).", 
      "comment_plain": "The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most (legacy spelling; see singular form, significantLink).", 
      "domains": [
        "WebPage"
      ], 
      "id": "significantLinks", 
      "label": "Significant Links", 
      "ranges": [
        "URL"
      ]
    }, 
    "skills": {
      "comment": "Skills required to fulfill this role.", 
      "comment_plain": "Skills required to fulfill this role.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "skills", 
      "label": "Skills", 
      "ranges": [
        "Text"
      ]
    }, 
    "sku": {
      "comment": "The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.", 
      "comment_plain": "The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.", 
      "domains": [
        "Product", 
        "Offer", 
        "Demand"
      ], 
      "id": "sku", 
      "label": "Sku", 
      "ranges": [
        "Text"
      ]
    }, 
    "sodiumContent": {
      "comment": "The number of milligrams of sodium.", 
      "comment_plain": "The number of milligrams of sodium.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "sodiumContent", 
      "label": "Sodium Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "softwareVersion": {
      "comment": "Version of the software instance.", 
      "comment_plain": "Version of the software instance.", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "softwareVersion", 
      "label": "Software Version", 
      "ranges": [
        "Text"
      ]
    }, 
    "source": {
      "comment": "The anatomical or organ system that the artery originates from.", 
      "comment_plain": "The anatomical or organ system that the artery originates from.", 
      "domains": [
        "Artery"
      ], 
      "id": "source", 
      "label": "Source", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "sourceOrganization": {
      "comment": "The Organization on whose behalf the creator was working.", 
      "comment_plain": "The Organization on whose behalf the creator was working.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "sourceOrganization", 
      "label": "Source Organization", 
      "ranges": [
        "Organization"
      ]
    }, 
    "sourcedFrom": {
      "comment": "The neurological pathway that originates the neurons.", 
      "comment_plain": "The neurological pathway that originates the neurons.", 
      "domains": [
        "Nerve"
      ], 
      "id": "sourcedFrom", 
      "label": "Sourced From", 
      "ranges": [
        "BrainStructure"
      ]
    }, 
    "spatial": {
      "comment": "The range of spatial applicability of a dataset, e.g. for a dataset of New York weather, the state of New York.", 
      "comment_plain": "The range of spatial applicability of a dataset, e.g. for a dataset of New York weather, the state of New York.", 
      "domains": [
        "Dataset"
      ], 
      "id": "spatial", 
      "label": "Spatial", 
      "ranges": [
        "Place"
      ]
    }, 
    "specialCommitments": {
      "comment": "Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.", 
      "comment_plain": "Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "specialCommitments", 
      "label": "Special Commitments", 
      "ranges": [
        "Text"
      ]
    }, 
    "specialty": {
      "comment": "One of the domain specialities to which this web page's content applies.", 
      "comment_plain": "One of the domain specialities to which this web page's content applies.", 
      "domains": [
        "WebPage"
      ], 
      "id": "specialty", 
      "label": "Specialty", 
      "ranges": [
        "Specialty"
      ]
    }, 
    "sponsor": {
      "comment": "Sponsor of the study.", 
      "comment_plain": "Sponsor of the study.", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "sponsor", 
      "label": "Sponsor", 
      "ranges": [
        "Organization"
      ]
    }, 
    "spouse": {
      "comment": "The person's spouse.", 
      "comment_plain": "The person's spouse.", 
      "domains": [
        "Person"
      ], 
      "id": "spouse", 
      "label": "Spouse", 
      "ranges": [
        "Person"
      ]
    }, 
    "stage": {
      "comment": "The stage of the condition, if applicable.", 
      "comment_plain": "The stage of the condition, if applicable.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "stage", 
      "label": "Stage", 
      "ranges": [
        "MedicalConditionStage"
      ]
    }, 
    "stageAsNumber": {
      "comment": "The stage represented as a number, e.g. 3.", 
      "comment_plain": "The stage represented as a number, e.g. 3.", 
      "domains": [
        "MedicalConditionStage"
      ], 
      "id": "stageAsNumber", 
      "label": "Stage As Number", 
      "ranges": [
        "Number"
      ]
    }, 
    "startDate": {
      "comment": "The start date and time of the event (in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 date format</a>).", 
      "comment_plain": "The start date and time of the event (in ISO 8601 date format).", 
      "domains": [
        "TVSeason", 
        "Event", 
        "TVSeries"
      ], 
      "id": "startDate", 
      "label": "Start Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "status": {
      "comment": "The status of the study (enumerated).", 
      "comment_plain": "The status of the study (enumerated).", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "status", 
      "label": "Status", 
      "ranges": [
        "MedicalStudyStatus"
      ]
    }, 
    "storageRequirements": {
      "comment": "Storage requirements (free space required).", 
      "comment_plain": "Storage requirements (free space required).", 
      "domains": [
        "SoftwareApplication"
      ], 
      "id": "storageRequirements", 
      "label": "Storage Requirements", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "streetAddress": {
      "comment": "The street address. For example, 1600 Amphitheatre Pkwy.", 
      "comment_plain": "The street address. For example, 1600 Amphitheatre Pkwy.", 
      "domains": [
        "PostalAddress"
      ], 
      "id": "streetAddress", 
      "label": "Street Address", 
      "ranges": [
        "Text"
      ]
    }, 
    "strengthUnit": {
      "comment": "The units of an active ingredient's strength, e.g. mg.", 
      "comment_plain": "The units of an active ingredient's strength, e.g. mg.", 
      "domains": [
        "DrugStrength"
      ], 
      "id": "strengthUnit", 
      "label": "Strength Unit", 
      "ranges": [
        "Text"
      ]
    }, 
    "strengthValue": {
      "comment": "The value of an active ingredient's strength, e.g. 325.", 
      "comment_plain": "The value of an active ingredient's strength, e.g. 325.", 
      "domains": [
        "DrugStrength"
      ], 
      "id": "strengthValue", 
      "label": "Strength Value", 
      "ranges": [
        "Number"
      ]
    }, 
    "structuralClass": {
      "comment": "The name given to how bone physically connects to each other.", 
      "comment_plain": "The name given to how bone physically connects to each other.", 
      "domains": [
        "Joint"
      ], 
      "id": "structuralClass", 
      "label": "Structural Class", 
      "ranges": [
        "Text"
      ]
    }, 
    "study": {
      "comment": "A medical study or trial related to this entity.", 
      "comment_plain": "A medical study or trial related to this entity.", 
      "domains": [
        "MedicalEntity"
      ], 
      "id": "study", 
      "label": "Study", 
      "ranges": [
        "MedicalStudy"
      ]
    }, 
    "studyDesign": {
      "comment": "Specifics about the observational study design (enumerated).", 
      "comment_plain": "Specifics about the observational study design (enumerated).", 
      "domains": [
        "MedicalObservationalStudy"
      ], 
      "id": "studyDesign", 
      "label": "Study Design", 
      "ranges": [
        "MedicalObservationalStudyDesign"
      ]
    }, 
    "studyLocation": {
      "comment": "The location in which the study is taking/took place.", 
      "comment_plain": "The location in which the study is taking/took place.", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "studyLocation", 
      "label": "Study Location", 
      "ranges": [
        "AdministrativeArea"
      ]
    }, 
    "studySubject": {
      "comment": "A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.", 
      "comment_plain": "A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.", 
      "domains": [
        "MedicalStudy"
      ], 
      "id": "studySubject", 
      "label": "Study Subject", 
      "ranges": [
        "MedicalEntity"
      ]
    }, 
    "subEvent": {
      "comment": "An Event that is part of this event. For example, a conference event includes many presentations, each are a subEvent of the conference.", 
      "comment_plain": "An Event that is part of this event. For example, a conference event includes many presentations, each are a subEvent of the conference.", 
      "domains": [
        "Event"
      ], 
      "id": "subEvent", 
      "label": "Sub Event", 
      "ranges": [
        "Event"
      ]
    }, 
    "subEvents": {
      "comment": "Events that are a part of this event. For example, a conference event includes many presentations, each are subEvents of the conference (legacy spelling; see singular form, subEvent).", 
      "comment_plain": "Events that are a part of this event. For example, a conference event includes many presentations, each are subEvents of the conference (legacy spelling; see singular form, subEvent).", 
      "domains": [
        "Event"
      ], 
      "id": "subEvents", 
      "label": "Sub Events", 
      "ranges": [
        "Event"
      ]
    }, 
    "subStageSuffix": {
      "comment": "The substage, e.g. 'a' for Stage IIIa.", 
      "comment_plain": "The substage, e.g. 'a' for Stage IIIa.", 
      "domains": [
        "MedicalConditionStage"
      ], 
      "id": "subStageSuffix", 
      "label": "Sub Stage Suffix", 
      "ranges": [
        "Text"
      ]
    }, 
    "subStructure": {
      "comment": "Component (sub-)structure(s) that comprise this anatomical structure.", 
      "comment_plain": "Component (sub-)structure(s) that comprise this anatomical structure.", 
      "domains": [
        "AnatomicalStructure"
      ], 
      "id": "subStructure", 
      "label": "Sub Structure", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "subTest": {
      "comment": "A component test of the panel.", 
      "comment_plain": "A component test of the panel.", 
      "domains": [
        "MedicalTestPanel"
      ], 
      "id": "subTest", 
      "label": "Sub Test", 
      "ranges": [
        "MedicalTest"
      ]
    }, 
    "subtype": {
      "comment": "A more specific type of the condition, where applicable, for example 'Type 1 Diabetes', 'Type 2 Diabetes', or 'Gestational Diabetes' for Diabetes.", 
      "comment_plain": "A more specific type of the condition, where applicable, for example 'Type 1 Diabetes', 'Type 2 Diabetes', or 'Gestational Diabetes' for Diabetes.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "subtype", 
      "label": "Subtype", 
      "ranges": [
        "Text"
      ]
    }, 
    "successorOf": {
      "comment": "A pointer from a newer variant of a product  to its previous, often discontinued predecessor.", 
      "comment_plain": "A pointer from a newer variant of a product  to its previous, often discontinued predecessor.", 
      "domains": [
        "ProductModel"
      ], 
      "id": "successorOf", 
      "label": "Successor of", 
      "ranges": [
        "ProductModel"
      ]
    }, 
    "sugarContent": {
      "comment": "The number of grams of sugar.", 
      "comment_plain": "The number of grams of sugar.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "sugarContent", 
      "label": "Sugar Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "suggestedGender": {
      "comment": "The gender of the person or audience.", 
      "comment_plain": "The gender of the person or audience.", 
      "domains": [
        "PeopleAudience"
      ], 
      "id": "suggestedGender", 
      "label": "Suggested Gender", 
      "ranges": [
        "Text"
      ]
    }, 
    "suggestedMaxAge": {
      "comment": "Maximal age recommended for viewing content", 
      "comment_plain": "Maximal age recommended for viewing content", 
      "domains": [
        "PeopleAudience"
      ], 
      "id": "suggestedMaxAge", 
      "label": "Suggested Max Age", 
      "ranges": [
        "Number"
      ]
    }, 
    "suggestedMinAge": {
      "comment": "Minimal age recommended for viewing content", 
      "comment_plain": "Minimal age recommended for viewing content", 
      "domains": [
        "PeopleAudience"
      ], 
      "id": "suggestedMinAge", 
      "label": "Suggested Min Age", 
      "ranges": [
        "Number"
      ]
    }, 
    "superEvent": {
      "comment": "An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.", 
      "comment_plain": "An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.", 
      "domains": [
        "Event"
      ], 
      "id": "superEvent", 
      "label": "Super Event", 
      "ranges": [
        "Event"
      ]
    }, 
    "supplyTo": {
      "comment": "The area to which the artery supplies blood to.", 
      "comment_plain": "The area to which the artery supplies blood to.", 
      "domains": [
        "Artery"
      ], 
      "id": "supplyTo", 
      "label": "Supply to", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "targetDescription": {
      "comment": "The description of a node in an established educational framework.", 
      "comment_plain": "The description of a node in an established educational framework.", 
      "domains": [
        "AlignmentObject"
      ], 
      "id": "targetDescription", 
      "label": "Target Description", 
      "ranges": [
        "Text"
      ]
    }, 
    "targetName": {
      "comment": "The name of a node in an established educational framework.", 
      "comment_plain": "The name of a node in an established educational framework.", 
      "domains": [
        "AlignmentObject"
      ], 
      "id": "targetName", 
      "label": "Target Name", 
      "ranges": [
        "Text"
      ]
    }, 
    "targetPlatform": {
      "comment": "Type of app development: phone, Metro style, desktop, XBox, etc.", 
      "comment_plain": "Type of app development: phone, Metro style, desktop, XBox, etc.", 
      "domains": [
        "APIReference"
      ], 
      "id": "targetPlatform", 
      "label": "Target Platform", 
      "ranges": [
        "Text"
      ]
    }, 
    "targetPopulation": {
      "comment": "Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.", 
      "comment_plain": "Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.", 
      "domains": [
        "DietarySupplement", 
        "DoseSchedule"
      ], 
      "id": "targetPopulation", 
      "label": "Target Population", 
      "ranges": [
        "Text"
      ]
    }, 
    "targetProduct": {
      "comment": "Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used.", 
      "comment_plain": "Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used.", 
      "domains": [
        "Code"
      ], 
      "id": "targetProduct", 
      "label": "Target Product", 
      "ranges": [
        "SoftwareApplication"
      ]
    }, 
    "targetUrl": {
      "comment": "The URL of a node in an established educational framework.", 
      "comment_plain": "The URL of a node in an established educational framework.", 
      "domains": [
        "AlignmentObject"
      ], 
      "id": "targetUrl", 
      "label": "Target Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "taxID": {
      "comment": "The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.", 
      "comment_plain": "The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "taxID", 
      "label": "Tax ID", 
      "ranges": [
        "Text"
      ]
    }, 
    "telephone": {
      "comment": "The telephone number.", 
      "comment_plain": "The telephone number.", 
      "domains": [
        "Organization", 
        "ContactPoint", 
        "Place", 
        "Person"
      ], 
      "id": "telephone", 
      "label": "Telephone", 
      "ranges": [
        "Text"
      ]
    }, 
    "temporal": {
      "comment": "The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).", 
      "comment_plain": "The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).", 
      "domains": [
        "Dataset"
      ], 
      "id": "temporal", 
      "label": "Temporal", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "text": {
      "comment": "The textual content of this CreativeWork.", 
      "comment_plain": "The textual content of this CreativeWork.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "text", 
      "label": "Text", 
      "ranges": [
        "Text"
      ]
    }, 
    "thumbnail": {
      "comment": "Thumbnail image for an image or video.", 
      "comment_plain": "Thumbnail image for an image or video.", 
      "domains": [
        "VideoObject", 
        "ImageObject"
      ], 
      "id": "thumbnail", 
      "label": "Thumbnail", 
      "ranges": [
        "ImageObject"
      ]
    }, 
    "thumbnailUrl": {
      "comment": "A thumbnail image relevant to the Thing.", 
      "comment_plain": "A thumbnail image relevant to the Thing.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "thumbnailUrl", 
      "label": "Thumbnail Url", 
      "ranges": [
        "URL"
      ]
    }, 
    "tickerSymbol": {
      "comment": "The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we reccommend using the controlled vocaulary of Market Identifier Codes (MIC) specified in ISO15022.", 
      "comment_plain": "The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we reccommend using the controlled vocaulary of Market Identifier Codes (MIC) specified in ISO15022.", 
      "domains": [
        "Corporation"
      ], 
      "id": "tickerSymbol", 
      "label": "Ticker Symbol", 
      "ranges": [
        "Text"
      ]
    }, 
    "timeRequired": {
      "comment": "Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. 'P30M', 'P1H25M'.", 
      "comment_plain": "Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. 'P30M', 'P1H25M'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "timeRequired", 
      "label": "Time Required", 
      "ranges": [
        "Duration"
      ]
    }, 
    "tissueSample": {
      "comment": "The type of tissue sample required for the test.", 
      "comment_plain": "The type of tissue sample required for the test.", 
      "domains": [
        "PathologyTest"
      ], 
      "id": "tissueSample", 
      "label": "Tissue Sample", 
      "ranges": [
        "Text"
      ]
    }, 
    "title": {
      "comment": "The title of the job.", 
      "comment_plain": "The title of the job.", 
      "domains": [
        "JobPosting"
      ], 
      "id": "title", 
      "label": "Title", 
      "ranges": [
        "Text"
      ]
    }, 
    "totalTime": {
      "comment": "The total time it takes to prepare and cook the recipe, in <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 duration format</a>.", 
      "comment_plain": "The total time it takes to prepare and cook the recipe, in ISO 8601 duration format.", 
      "domains": [
        "Recipe"
      ], 
      "id": "totalTime", 
      "label": "Total Time", 
      "ranges": [
        "Duration"
      ]
    }, 
    "track": {
      "comment": "A music recording (track)\u2014usually a single song.", 
      "comment_plain": "A music recording (track)\u2014usually a single song.", 
      "domains": [
        "MusicPlaylist", 
        "MusicGroup"
      ], 
      "id": "track", 
      "label": "Track", 
      "ranges": [
        "MusicRecording"
      ]
    }, 
    "tracks": {
      "comment": "A music recording (track)\u2014usually a single song (legacy spelling; see singular form, track).", 
      "comment_plain": "A music recording (track)\u2014usually a single song (legacy spelling; see singular form, track).", 
      "domains": [
        "MusicPlaylist", 
        "MusicGroup"
      ], 
      "id": "tracks", 
      "label": "Tracks", 
      "ranges": [
        "MusicRecording"
      ]
    }, 
    "trailer": {
      "comment": "The trailer of the movie or TV series, season, or episode.", 
      "comment_plain": "The trailer of the movie or TV series, season, or episode.", 
      "domains": [
        "TVEpisode", 
        "Movie", 
        "TVSeries", 
        "TVSeason"
      ], 
      "id": "trailer", 
      "label": "Trailer", 
      "ranges": [
        "VideoObject"
      ]
    }, 
    "transFatContent": {
      "comment": "The number of grams of trans fat.", 
      "comment_plain": "The number of grams of trans fat.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "transFatContent", 
      "label": "Trans Fat Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "transcript": {
      "comment": "If this MediaObject is an AudioObject or VideoObject, the transcript of that object.", 
      "comment_plain": "If this MediaObject is an AudioObject or VideoObject, the transcript of that object.", 
      "domains": [
        "AudioObject", 
        "VideoObject"
      ], 
      "id": "transcript", 
      "label": "Transcript", 
      "ranges": [
        "Text"
      ]
    }, 
    "transmissionMethod": {
      "comment": "How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.", 
      "comment_plain": "How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.", 
      "domains": [
        "InfectiousDisease"
      ], 
      "id": "transmissionMethod", 
      "label": "Transmission Method", 
      "ranges": [
        "Text"
      ]
    }, 
    "trialDesign": {
      "comment": "Specifics about the trial design (enumerated).", 
      "comment_plain": "Specifics about the trial design (enumerated).", 
      "domains": [
        "MedicalTrial"
      ], 
      "id": "trialDesign", 
      "label": "Trial Design", 
      "ranges": [
        "MedicalTrialDesign"
      ]
    }, 
    "tributary": {
      "comment": "The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.", 
      "comment_plain": "The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.", 
      "domains": [
        "Vein"
      ], 
      "id": "tributary", 
      "label": "Tributary", 
      "ranges": [
        "AnatomicalStructure"
      ]
    }, 
    "typeOfGood": {
      "comment": "The product that this structured value is referring to.", 
      "comment_plain": "The product that this structured value is referring to.", 
      "domains": [
        "OwnershipInfo", 
        "TypeAndQuantityNode"
      ], 
      "id": "typeOfGood", 
      "label": "Type of Good", 
      "ranges": [
        "Product"
      ]
    }, 
    "typicalAgeRange": {
      "comment": "The typical range of ages the content's intendedEndUser, for example '7-9', '11-'.", 
      "comment_plain": "The typical range of ages the content's intendedEndUser, for example '7-9', '11-'.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "typicalAgeRange", 
      "label": "Typical Age Range", 
      "ranges": [
        "Text"
      ]
    }, 
    "typicalTest": {
      "comment": "A medical test typically performed given this condition.", 
      "comment_plain": "A medical test typically performed given this condition.", 
      "domains": [
        "MedicalCondition"
      ], 
      "id": "typicalTest", 
      "label": "Typical Test", 
      "ranges": [
        "MedicalTest"
      ]
    }, 
    "unitCode": {
      "comment": "The unit of measurement given using the UN/CEFACT Common Code (3 characters).", 
      "comment_plain": "The unit of measurement given using the UN/CEFACT Common Code (3 characters).", 
      "domains": [
        "TypeAndQuantityNode", 
        "QuantitativeValue", 
        "UnitPriceSpecification"
      ], 
      "id": "unitCode", 
      "label": "Unit Code", 
      "ranges": [
        "Text"
      ]
    }, 
    "unsaturatedFatContent": {
      "comment": "The number of grams of unsaturated fat.", 
      "comment_plain": "The number of grams of unsaturated fat.", 
      "domains": [
        "NutritionInformation"
      ], 
      "id": "unsaturatedFatContent", 
      "label": "Unsaturated Fat Content", 
      "ranges": [
        "Mass"
      ]
    }, 
    "uploadDate": {
      "comment": "Date when this media object was uploaded to this site.", 
      "comment_plain": "Date when this media object was uploaded to this site.", 
      "domains": [
        "MediaObject"
      ], 
      "id": "uploadDate", 
      "label": "Upload Date", 
      "ranges": [
        "Date"
      ]
    }, 
    "url": {
      "comment": "URL of the item.", 
      "comment_plain": "URL of the item.", 
      "domains": [
        "Thing"
      ], 
      "id": "url", 
      "label": "URL", 
      "ranges": [
        "URL"
      ]
    }, 
    "usedToDiagnose": {
      "comment": "A condition the test is used to diagnose.", 
      "comment_plain": "A condition the test is used to diagnose.", 
      "domains": [
        "MedicalTest"
      ], 
      "id": "usedToDiagnose", 
      "label": "Used to Diagnose", 
      "ranges": [
        "MedicalCondition"
      ]
    }, 
    "usesDevice": {
      "comment": "Device used to perform the test.", 
      "comment_plain": "Device used to perform the test.", 
      "domains": [
        "MedicalTest"
      ], 
      "id": "usesDevice", 
      "label": "Uses Device", 
      "ranges": [
        "MedicalDevice"
      ]
    }, 
    "validFrom": {
      "comment": "The beginning of the validity of offer, price specification, or opening hours data.", 
      "comment_plain": "The beginning of the validity of offer, price specification, or opening hours data.", 
      "domains": [
        "OpeningHoursSpecification", 
        "Demand", 
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "validFrom", 
      "label": "Valid From", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "validThrough": {
      "comment": "The end of the validity of offer, price specification, or opening hours data.", 
      "comment_plain": "The end of the validity of offer, price specification, or opening hours data.", 
      "domains": [
        "OpeningHoursSpecification", 
        "Demand", 
        "PriceSpecification", 
        "Offer"
      ], 
      "id": "validThrough", 
      "label": "Valid Through", 
      "ranges": [
        "DateTime"
      ]
    }, 
    "value": {
      "comment": "The value of the product characteristic.", 
      "comment_plain": "The value of the product characteristic.", 
      "domains": [
        "QuantitativeValue"
      ], 
      "id": "value", 
      "label": "Value", 
      "ranges": [
        "Number"
      ]
    }, 
    "valueAddedTaxIncluded": {
      "comment": "Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.", 
      "comment_plain": "Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.", 
      "domains": [
        "PriceSpecification"
      ], 
      "id": "valueAddedTaxIncluded", 
      "label": "Value Added Tax Included", 
      "ranges": [
        "Boolean"
      ]
    }, 
    "valueReference": {
      "comment": "A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.", 
      "comment_plain": "A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.", 
      "domains": [
        "QualitativeValue", 
        "QuantitativeValue"
      ], 
      "id": "valueReference", 
      "label": "Value Reference", 
      "ranges": [
        "Enumeration", 
        "StructuredValue"
      ]
    }, 
    "vatID": {
      "comment": "The Value-added Tax ID of the organisation or person.", 
      "comment_plain": "The Value-added Tax ID of the organisation or person.", 
      "domains": [
        "Organization", 
        "Person"
      ], 
      "id": "vatID", 
      "label": "Vat ID", 
      "ranges": [
        "Text"
      ]
    }, 
    "version": {
      "comment": "The version of the CreativeWork embodied by a specified resource.", 
      "comment_plain": "The version of the CreativeWork embodied by a specified resource.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "version", 
      "label": "Version", 
      "ranges": [
        "Number"
      ]
    }, 
    "video": {
      "comment": "An embedded video object.", 
      "comment_plain": "An embedded video object.", 
      "domains": [
        "CreativeWork"
      ], 
      "id": "video", 
      "label": "Video", 
      "ranges": [
        "VideoObject"
      ]
    }, 
    "videoFrameSize": {
      "comment": "The frame size of the video.", 
      "comment_plain": "The frame size of the video.", 
      "domains": [
        "VideoObject"
      ], 
      "id": "videoFrameSize", 
      "label": "Video Frame Size", 
      "ranges": [
        "Text"
      ]
    }, 
    "videoQuality": {
      "comment": "The quality of the video.", 
      "comment_plain": "The quality of the video.", 
      "domains": [
        "VideoObject"
      ], 
      "id": "videoQuality", 
      "label": "Video Quality", 
      "ranges": [
        "Text"
      ]
    }, 
    "warning": {
      "comment": "Any FDA or other warnings about the drug (text or URL).", 
      "comment_plain": "Any FDA or other warnings about the drug (text or URL).", 
      "domains": [
        "Drug"
      ], 
      "id": "warning", 
      "label": "Warning", 
      "ranges": [
        "Text", 
        "URL"
      ]
    }, 
    "warranty": {
      "comment": "The warranty promise(s) included in the offer.", 
      "comment_plain": "The warranty promise(s) included in the offer.", 
      "domains": [
        "Offer", 
        "Demand"
      ], 
      "id": "warranty", 
      "label": "Warranty", 
      "ranges": [
        "WarrantyPromise"
      ]
    }, 
    "warrantyScope": {
      "comment": "The scope of the warranty promise.", 
      "comment_plain": "The scope of the warranty promise.", 
      "domains": [
        "WarrantyPromise"
      ], 
      "id": "warrantyScope", 
      "label": "Warranty Scope", 
      "ranges": [
        "WarrantyScope"
      ]
    }, 
    "weight": {
      "comment": "The weight of the product.", 
      "comment_plain": "The weight of the product.", 
      "domains": [
        "Product"
      ], 
      "id": "weight", 
      "label": "Weight", 
      "ranges": [
        "QuantitativeValue"
      ]
    }, 
    "width": {
      "comment": "The width of the item.", 
      "comment_plain": "The width of the item.", 
      "domains": [
        "MediaObject", 
        "Product"
      ], 
      "id": "width", 
      "label": "Width", 
      "ranges": [
        "Distance", 
        "QuantitativeValue"
      ]
    }, 
    "wordCount": {
      "comment": "The number of words in the text of the Article.", 
      "comment_plain": "The number of words in the text of the Article.", 
      "domains": [
        "Article"
      ], 
      "id": "wordCount", 
      "label": "Word Count", 
      "ranges": [
        "Integer"
      ]
    }, 
    "workHours": {
      "comment": "The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).", 
      "comment_plain": "The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).", 
      "domains": [
        "JobPosting"
      ], 
      "id": "workHours", 
      "label": "Work Hours", 
      "ranges": [
        "Text"
      ]
    }, 
    "workLocation": {
      "comment": "A contact location for a person's place of work.", 
      "comment_plain": "A contact location for a person's place of work.", 
      "domains": [
        "Person"
      ], 
      "id": "workLocation", 
      "label": "Work Location", 
      "ranges": [
        "ContactPoint", 
        "Place"
      ]
    }, 
    "workload": {
      "comment": "Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.", 
      "comment_plain": "Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.", 
      "domains": [
        "ExercisePlan"
      ], 
      "id": "workload", 
      "label": "Workload", 
      "ranges": [
        "Energy"
      ]
    }, 
    "worksFor": {
      "comment": "Organizations that the person works for.", 
      "comment_plain": "Organizations that the person works for.", 
      "domains": [
        "Person"
      ], 
      "id": "worksFor", 
      "label": "Works for", 
      "ranges": [
        "Organization"
      ]
    }, 
    "worstRating": {
      "comment": "The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.", 
      "comment_plain": "The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.", 
      "domains": [
        "Rating"
      ], 
      "id": "worstRating", 
      "label": "Worst Rating", 
      "ranges": [
        "Number", 
        "Text"
      ]
    }
  }, 
  "types": {
    "APIReference": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article", 
        "TechArticle"
      ], 
      "comment": "Reference documentation for application programming interfaces (APIs).", 
      "comment_plain": "Reference documentation for application programming interfaces (APIs).", 
      "id": "APIReference", 
      "label": "API Reference", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount", 
        "dependencies", 
        "proficiencyLevel", 
        "assembly", 
        "assemblyVersion", 
        "programmingModel", 
        "targetPlatform"
      ], 
      "specific_properties": [
        "assembly", 
        "assemblyVersion", 
        "programmingModel", 
        "targetPlatform"
      ], 
      "subtypes": [], 
      "supertypes": [
        "TechArticle"
      ], 
      "url": "http://schema.org/APIReference"
    }, 
    "AboutPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: About page.", 
      "comment_plain": "Web page type: About page.", 
      "id": "AboutPage", 
      "label": "About Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/AboutPage"
    }, 
    "AccountingService": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FinancialService"
      ], 
      "comment": "Accountancy business.", 
      "comment_plain": "Accountancy business.", 
      "id": "AccountingService", 
      "label": "Accounting Service", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "FinancialService"
      ], 
      "url": "http://schema.org/AccountingService"
    }, 
    "AdministrativeArea": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "A geographical region under the jurisdiction of a particular government.", 
      "comment_plain": "A geographical region under the jurisdiction of a particular government.", 
      "id": "AdministrativeArea", 
      "label": "Administrative Area", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "City", 
        "Country", 
        "State"
      ], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/AdministrativeArea"
    }, 
    "AdultEntertainment": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "An adult entertainment establishment.", 
      "comment_plain": "An adult entertainment establishment.", 
      "id": "AdultEntertainment", 
      "label": "Adult Entertainment", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/AdultEntertainment"
    }, 
    "AggregateOffer": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Offer"
      ], 
      "comment": "When a single product that has different offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.", 
      "comment_plain": "When a single product that has different offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.", 
      "id": "AggregateOffer", 
      "label": "Aggregate Offer", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "acceptedPaymentMethod", 
        "addOn", 
        "advanceBookingRequirement", 
        "aggregateRating", 
        "availability", 
        "availabilityEnds", 
        "availabilityStarts", 
        "availableAtOrFrom", 
        "availableDeliveryMethod", 
        "businessFunction", 
        "category", 
        "deliveryLeadTime", 
        "eligibleCustomerType", 
        "eligibleDuration", 
        "eligibleQuantity", 
        "eligibleRegion", 
        "eligibleTransactionVolume", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "includesObject", 
        "inventoryLevel", 
        "itemCondition", 
        "itemOffered", 
        "mpn", 
        "price", 
        "priceCurrency", 
        "priceSpecification", 
        "priceValidUntil", 
        "review", 
        "reviews", 
        "seller", 
        "serialNumber", 
        "sku", 
        "validFrom", 
        "validThrough", 
        "warranty", 
        "highPrice", 
        "lowPrice", 
        "offerCount"
      ], 
      "specific_properties": [
        "highPrice", 
        "lowPrice", 
        "offerCount"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Offer"
      ], 
      "url": "http://schema.org/AggregateOffer"
    }, 
    "AggregateRating": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Rating"
      ], 
      "comment": "The average rating based on multiple ratings or reviews.", 
      "comment_plain": "The average rating based on multiple ratings or reviews.", 
      "id": "AggregateRating", 
      "label": "Aggregate Rating", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "bestRating", 
        "ratingValue", 
        "worstRating", 
        "itemReviewed", 
        "ratingCount", 
        "reviewCount"
      ], 
      "specific_properties": [
        "itemReviewed", 
        "ratingCount", 
        "reviewCount"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Rating"
      ], 
      "url": "http://schema.org/AggregateRating"
    }, 
    "Airport": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "An airport.", 
      "comment_plain": "An airport.", 
      "id": "Airport", 
      "label": "Airport", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Airport"
    }, 
    "AlignmentObject": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "An intangible item that describes an alignment between a learning resource and a node in an educational framework.", 
      "comment_plain": "An intangible item that describes an alignment between a learning resource and a node in an educational framework.", 
      "id": "AlignmentObject", 
      "label": "Alignment Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alignmentType", 
        "educationalFramework", 
        "targetDescription", 
        "targetName", 
        "targetUrl"
      ], 
      "specific_properties": [
        "alignmentType", 
        "educationalFramework", 
        "targetDescription", 
        "targetName", 
        "targetUrl"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/AlignmentObject"
    }, 
    "AmusementPark": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "An amusement park.", 
      "comment_plain": "An amusement park.", 
      "id": "AmusementPark", 
      "label": "Amusement Park", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/AmusementPark"
    }, 
    "AnatomicalStructure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.", 
      "comment_plain": "Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.", 
      "id": "AnatomicalStructure", 
      "label": "Anatomical Structure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "specific_properties": [
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "subtypes": [
        "Bone", 
        "BrainStructure", 
        "Joint", 
        "Ligament", 
        "Muscle", 
        "Nerve", 
        "Vessel"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/AnatomicalStructure"
    }, 
    "AnatomicalSystem": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can includes circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.", 
      "comment_plain": "An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can includes circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.", 
      "id": "AnatomicalSystem", 
      "label": "Anatomical System", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "comprisedOf", 
        "relatedCondition", 
        "relatedStructure", 
        "relatedTherapy"
      ], 
      "specific_properties": [
        "associatedPathophysiology", 
        "comprisedOf", 
        "relatedCondition", 
        "relatedStructure", 
        "relatedTherapy"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/AnatomicalSystem"
    }, 
    "AnimalShelter": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Animal shelter.", 
      "comment_plain": "Animal shelter.", 
      "id": "AnimalShelter", 
      "label": "Animal Shelter", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/AnimalShelter"
    }, 
    "ApartmentComplex": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Residence"
      ], 
      "comment": "Residence type: Apartment complex.", 
      "comment_plain": "Residence type: Apartment complex.", 
      "id": "ApartmentComplex", 
      "label": "Apartment Complex", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Residence"
      ], 
      "url": "http://schema.org/ApartmentComplex"
    }, 
    "ApprovedIndication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIndication"
      ], 
      "comment": "An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.", 
      "comment_plain": "An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.", 
      "id": "ApprovedIndication", 
      "label": "Approved Indication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIndication"
      ], 
      "url": "http://schema.org/ApprovedIndication"
    }, 
    "Aquarium": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "Aquarium.", 
      "comment_plain": "Aquarium.", 
      "id": "Aquarium", 
      "label": "Aquarium", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Aquarium"
    }, 
    "ArtGallery": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "An art gallery.", 
      "comment_plain": "An art gallery.", 
      "id": "ArtGallery", 
      "label": "Art Gallery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/ArtGallery"
    }, 
    "Artery": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure", 
        "Vessel"
      ], 
      "comment": "A type of blood vessel that specifically carries blood away from the heart.", 
      "comment_plain": "A type of blood vessel that specifically carries blood away from the heart.", 
      "id": "Artery", 
      "label": "Artery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "arterialBranch", 
        "source", 
        "supplyTo"
      ], 
      "specific_properties": [
        "arterialBranch", 
        "source", 
        "supplyTo"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Vessel"
      ], 
      "url": "http://schema.org/Artery"
    }, 
    "Article": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.", 
      "comment_plain": "An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.", 
      "id": "Article", 
      "label": "Article", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount"
      ], 
      "specific_properties": [
        "articleBody", 
        "articleSection", 
        "wordCount"
      ], 
      "subtypes": [
        "BlogPosting", 
        "NewsArticle", 
        "ScholarlyArticle", 
        "TechArticle"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Article"
    }, 
    "Attorney": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "ProfessionalService"
      ], 
      "comment": "Professional service: Attorney.", 
      "comment_plain": "Professional service: Attorney.", 
      "id": "Attorney", 
      "label": "Attorney", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService"
      ], 
      "url": "http://schema.org/Attorney"
    }, 
    "Audience": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "Intended audience for an item, i.e. the group for whom the item was created.", 
      "comment_plain": "Intended audience for an item, i.e. the group for whom the item was created.", 
      "id": "Audience", 
      "instances": [
        "Researcher"
      ], 
      "label": "Audience", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "EducationalAudience", 
        "MedicalAudience", 
        "PeopleAudience"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Audience"
    }, 
    "AudioObject": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MediaObject"
      ], 
      "comment": "An audio file.", 
      "comment_plain": "An audio file.", 
      "id": "AudioObject", 
      "label": "Audio Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width", 
        "transcript"
      ], 
      "specific_properties": [
        "transcript"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MediaObject"
      ], 
      "url": "http://schema.org/AudioObject"
    }, 
    "AutoBodyShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "Auto body shop.", 
      "comment_plain": "Auto body shop.", 
      "id": "AutoBodyShop", 
      "label": "Auto Body Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/AutoBodyShop"
    }, 
    "AutoDealer": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "An car dealership.", 
      "comment_plain": "An car dealership.", 
      "id": "AutoDealer", 
      "label": "Auto Dealer", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/AutoDealer"
    }, 
    "AutoPartsStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "An auto parts store.", 
      "comment_plain": "An auto parts store.", 
      "id": "AutoPartsStore", 
      "label": "Auto Parts Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness", 
        "Store"
      ], 
      "url": "http://schema.org/AutoPartsStore"
    }, 
    "AutoRental": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "A car rental business.", 
      "comment_plain": "A car rental business.", 
      "id": "AutoRental", 
      "label": "Auto Rental", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/AutoRental"
    }, 
    "AutoRepair": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "Car repair business.", 
      "comment_plain": "Car repair business.", 
      "id": "AutoRepair", 
      "label": "Auto Repair", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/AutoRepair"
    }, 
    "AutoWash": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "A car wash business.", 
      "comment_plain": "A car wash business.", 
      "id": "AutoWash", 
      "label": "Auto Wash", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/AutoWash"
    }, 
    "AutomatedTeller": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FinancialService"
      ], 
      "comment": "ATM/cash machine.", 
      "comment_plain": "ATM/cash machine.", 
      "id": "AutomatedTeller", 
      "label": "Automated Teller", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FinancialService"
      ], 
      "url": "http://schema.org/AutomatedTeller"
    }, 
    "AutomotiveBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Car repair, sales, or parts.", 
      "comment_plain": "Car repair, sales, or parts.", 
      "id": "AutomotiveBusiness", 
      "label": "Automotive Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AutoBodyShop", 
        "AutoDealer", 
        "AutoPartsStore", 
        "AutoRental", 
        "AutoRepair", 
        "AutoWash", 
        "GasStation", 
        "MotorcycleDealer", 
        "MotorcycleRepair"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/AutomotiveBusiness"
    }, 
    "Bakery": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A bakery.", 
      "comment_plain": "A bakery.", 
      "id": "Bakery", 
      "label": "Bakery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/Bakery"
    }, 
    "BankOrCreditUnion": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FinancialService"
      ], 
      "comment": "Bank or credit union.", 
      "comment_plain": "Bank or credit union.", 
      "id": "BankOrCreditUnion", 
      "label": "Bank or Credit Union", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FinancialService"
      ], 
      "url": "http://schema.org/BankOrCreditUnion"
    }, 
    "BarOrPub": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A bar or pub.", 
      "comment_plain": "A bar or pub.", 
      "id": "BarOrPub", 
      "label": "Bar or Pub", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/BarOrPub"
    }, 
    "Beach": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "Beach.", 
      "comment_plain": "Beach.", 
      "id": "Beach", 
      "label": "Beach", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Beach"
    }, 
    "BeautySalon": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "Beauty salon.", 
      "comment_plain": "Beauty salon.", 
      "id": "BeautySalon", 
      "label": "Beauty Salon", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness"
      ], 
      "url": "http://schema.org/BeautySalon"
    }, 
    "BedAndBreakfast": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "LodgingBusiness"
      ], 
      "comment": "Bed and breakfast.", 
      "comment_plain": "Bed and breakfast.", 
      "id": "BedAndBreakfast", 
      "label": "Bed And Breakfast", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LodgingBusiness"
      ], 
      "url": "http://schema.org/BedAndBreakfast"
    }, 
    "BikeStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A bike store.", 
      "comment_plain": "A bike store.", 
      "id": "BikeStore", 
      "label": "Bike Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/BikeStore"
    }, 
    "Blog": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A blog", 
      "comment_plain": "A blog", 
      "id": "Blog", 
      "label": "Blog", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "blogPost", 
        "blogPosts"
      ], 
      "specific_properties": [
        "blogPost", 
        "blogPosts"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Blog"
    }, 
    "BlogPosting": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article"
      ], 
      "comment": "A blog post.", 
      "comment_plain": "A blog post.", 
      "id": "BlogPosting", 
      "label": "Blog Posting", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Article"
      ], 
      "url": "http://schema.org/BlogPosting"
    }, 
    "BloodTest": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTest"
      ], 
      "comment": "A medical test performed on a sample of a patient's blood.", 
      "comment_plain": "A medical test performed on a sample of a patient's blood.", 
      "id": "BloodTest", 
      "label": "Blood Test", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTest"
      ], 
      "url": "http://schema.org/BloodTest"
    }, 
    "BodyOfWater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform"
      ], 
      "comment": "A body of water, such as a sea, ocean, or lake.", 
      "comment_plain": "A body of water, such as a sea, ocean, or lake.", 
      "id": "BodyOfWater", 
      "label": "Body of Water", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Canal", 
        "LakeBodyOfWater", 
        "OceanBodyOfWater", 
        "Pond", 
        "Reservoir", 
        "RiverBodyOfWater", 
        "SeaBodyOfWater", 
        "Waterfall"
      ], 
      "supertypes": [
        "Landform"
      ], 
      "url": "http://schema.org/BodyOfWater"
    }, 
    "Bone": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "Rigid connective tissue that comprises up the skeletal structure of the human body.", 
      "comment_plain": "Rigid connective tissue that comprises up the skeletal structure of the human body.", 
      "id": "Bone", 
      "label": "Bone", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Bone"
    }, 
    "Book": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A book.", 
      "comment_plain": "A book.", 
      "id": "Book", 
      "label": "Book", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "bookEdition", 
        "bookFormat", 
        "illustrator", 
        "isbn", 
        "numberOfPages"
      ], 
      "specific_properties": [
        "bookEdition", 
        "bookFormat", 
        "illustrator", 
        "isbn", 
        "numberOfPages"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Book"
    }, 
    "BookFormatType": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "The publication format of the book.", 
      "comment_plain": "The publication format of the book.", 
      "id": "BookFormatType", 
      "instances": [
        "EBook", 
        "Hardcover", 
        "Paperback"
      ], 
      "label": "Book Format Type", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/BookFormatType"
    }, 
    "BookStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A bookstore.", 
      "comment_plain": "A bookstore.", 
      "id": "BookStore", 
      "label": "Book Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/BookStore"
    }, 
    "BowlingAlley": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A bowling alley.", 
      "comment_plain": "A bowling alley.", 
      "id": "BowlingAlley", 
      "label": "Bowling Alley", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/BowlingAlley"
    }, 
    "BrainStructure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.", 
      "comment_plain": "Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.", 
      "id": "BrainStructure", 
      "label": "Brain Structure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/BrainStructure"
    }, 
    "Brand": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "A brand is a name used by an organization or business person for labeling a product, product group, or similar.", 
      "comment_plain": "A brand is a name used by an organization or business person for labeling a product, product group, or similar.", 
      "id": "Brand", 
      "label": "Brand", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "logo"
      ], 
      "specific_properties": [
        "logo"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Brand"
    }, 
    "Brewery": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "Brewery.", 
      "comment_plain": "Brewery.", 
      "id": "Brewery", 
      "label": "Brewery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/Brewery"
    }, 
    "BuddhistTemple": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A Buddhist temple.", 
      "comment_plain": "A Buddhist temple.", 
      "id": "BuddhistTemple", 
      "label": "Buddhist Temple", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/BuddhistTemple"
    }, 
    "BusStation": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A bus station.", 
      "comment_plain": "A bus station.", 
      "id": "BusStation", 
      "label": "Bus Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/BusStation"
    }, 
    "BusStop": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A bus stop.", 
      "comment_plain": "A bus stop.", 
      "id": "BusStop", 
      "label": "Bus Stop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/BusStop"
    }, 
    "BusinessEntityType": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Business\nhttp://purl.org/goodrelations/v1#Enduser\nhttp://purl.org/goodrelations/v1#PublicInstitution\nhttp://purl.org/goodrelations/v1#Reseller", 
      "comment_plain": "A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Business\nhttp://purl.org/goodrelations/v1#Enduser\nhttp://purl.org/goodrelations/v1#PublicInstitution\nhttp://purl.org/goodrelations/v1#Reseller", 
      "id": "BusinessEntityType", 
      "label": "Business Entity Type", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/BusinessEntityType"
    }, 
    "BusinessEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Business event.", 
      "comment_plain": "Event type: Business event.", 
      "id": "BusinessEvent", 
      "label": "Business Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/BusinessEvent"
    }, 
    "BusinessFunction": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#ConstructionInstallation\nhttp://purl.org/goodrelations/v1#Dispose\nhttp://purl.org/goodrelations/v1#LeaseOut\nhttp://purl.org/goodrelations/v1#Maintain\nhttp://purl.org/goodrelations/v1#ProvideService\nhttp://purl.org/goodrelations/v1#Repair\nhttp://purl.org/goodrelations/v1#Sell\nhttp://purl.org/goodrelations/v1#Buy", 
      "comment_plain": "The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#ConstructionInstallation\nhttp://purl.org/goodrelations/v1#Dispose\nhttp://purl.org/goodrelations/v1#LeaseOut\nhttp://purl.org/goodrelations/v1#Maintain\nhttp://purl.org/goodrelations/v1#ProvideService\nhttp://purl.org/goodrelations/v1#Repair\nhttp://purl.org/goodrelations/v1#Sell\nhttp://purl.org/goodrelations/v1#Buy", 
      "id": "BusinessFunction", 
      "label": "Business Function", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/BusinessFunction"
    }, 
    "CafeOrCoffeeShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A cafe or coffee shop.", 
      "comment_plain": "A cafe or coffee shop.", 
      "id": "CafeOrCoffeeShop", 
      "label": "Cafe or Coffee Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/CafeOrCoffeeShop"
    }, 
    "Campground": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A campground.", 
      "comment_plain": "A campground.", 
      "id": "Campground", 
      "label": "Campground", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Campground"
    }, 
    "Canal": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A canal, like the Panama Canal", 
      "comment_plain": "A canal, like the Panama Canal", 
      "id": "Canal", 
      "label": "Canal", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/Canal"
    }, 
    "Casino": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "A casino.", 
      "comment_plain": "A casino.", 
      "id": "Casino", 
      "label": "Casino", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/Casino"
    }, 
    "CatholicChurch": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A Catholic church.", 
      "comment_plain": "A Catholic church.", 
      "id": "CatholicChurch", 
      "label": "Catholic Church", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/CatholicChurch"
    }, 
    "Cemetery": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A graveyard.", 
      "comment_plain": "A graveyard.", 
      "id": "Cemetery", 
      "label": "Cemetery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Cemetery"
    }, 
    "CheckoutPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: Checkout page.", 
      "comment_plain": "Web page type: Checkout page.", 
      "id": "CheckoutPage", 
      "label": "Checkout Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/CheckoutPage"
    }, 
    "ChildCare": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A Childcare center.", 
      "comment_plain": "A Childcare center.", 
      "id": "ChildCare", 
      "label": "Child Care", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/ChildCare"
    }, 
    "ChildrensEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Children's event.", 
      "comment_plain": "Event type: Children's event.", 
      "id": "ChildrensEvent", 
      "label": "Childrens Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/ChildrensEvent"
    }, 
    "Church": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A church.", 
      "comment_plain": "A church.", 
      "id": "Church", 
      "label": "Church", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/Church"
    }, 
    "City": {
      "ancestors": [
        "Thing", 
        "Place", 
        "AdministrativeArea"
      ], 
      "comment": "A city or town.", 
      "comment_plain": "A city or town.", 
      "id": "City", 
      "label": "City", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AdministrativeArea"
      ], 
      "url": "http://schema.org/City"
    }, 
    "CityHall": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "GovernmentBuilding"
      ], 
      "comment": "A city hall.", 
      "comment_plain": "A city hall.", 
      "id": "CityHall", 
      "label": "City Hall", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentBuilding"
      ], 
      "url": "http://schema.org/CityHall"
    }, 
    "CivicStructure": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "A public structure, such as a town hall or concert hall.", 
      "comment_plain": "A public structure, such as a town hall or concert hall.", 
      "id": "CivicStructure", 
      "label": "Civic Structure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [
        "openingHours"
      ], 
      "subtypes": [
        "Airport", 
        "Aquarium", 
        "Beach", 
        "BusStation", 
        "BusStop", 
        "Campground", 
        "Cemetery", 
        "Crematorium", 
        "EventVenue", 
        "FireStation", 
        "GovernmentBuilding", 
        "Hospital", 
        "MovieTheater", 
        "Museum", 
        "MusicVenue", 
        "Park", 
        "ParkingFacility", 
        "PerformingArtsTheater", 
        "PlaceOfWorship", 
        "Playground", 
        "PoliceStation", 
        "RVPark", 
        "StadiumOrArena", 
        "SubwayStation", 
        "TaxiStand", 
        "TrainStation", 
        "Zoo"
      ], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/CivicStructure"
    }, 
    "Class": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "A class, also often called a 'Type'; equivalent to rdfs:Class.", 
      "comment_plain": "A class, also often called a 'Type'; equivalent to rdfs:Class.", 
      "id": "Class", 
      "label": "Class", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Class"
    }, 
    "ClothingStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A clothing store.", 
      "comment_plain": "A clothing store.", 
      "id": "ClothingStore", 
      "label": "Clothing Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ClothingStore"
    }, 
    "Code": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.", 
      "comment_plain": "Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.", 
      "id": "Code", 
      "label": "Code", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "codeRepository", 
        "programmingLanguage", 
        "runtime", 
        "sampleType", 
        "targetProduct"
      ], 
      "specific_properties": [
        "codeRepository", 
        "programmingLanguage", 
        "runtime", 
        "sampleType", 
        "targetProduct"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Code"
    }, 
    "CollectionPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: Collection page.", 
      "comment_plain": "Web page type: Collection page.", 
      "id": "CollectionPage", 
      "label": "Collection Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "ImageGallery", 
        "VideoGallery"
      ], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/CollectionPage"
    }, 
    "CollegeOrUniversity": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "A college, university, or other third-level educational institution.", 
      "comment_plain": "A college, university, or other third-level educational institution.", 
      "id": "CollegeOrUniversity", 
      "label": "College or University", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/CollegeOrUniversity"
    }, 
    "ComedyClub": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "A comedy club.", 
      "comment_plain": "A comedy club.", 
      "id": "ComedyClub", 
      "label": "Comedy Club", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/ComedyClub"
    }, 
    "ComedyEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Comedy event.", 
      "comment_plain": "Event type: Comedy event.", 
      "id": "ComedyEvent", 
      "label": "Comedy Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/ComedyEvent"
    }, 
    "Comment": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the \"text\" property, and its topic via \"about\", properties shared with all CreativeWorks.", 
      "comment_plain": "A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the \"text\" property, and its topic via \"about\", properties shared with all CreativeWorks.", 
      "id": "Comment", 
      "label": "Comment", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Comment"
    }, 
    "ComputerStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A computer store.", 
      "comment_plain": "A computer store.", 
      "id": "ComputerStore", 
      "label": "Computer Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ComputerStore"
    }, 
    "ContactPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: Contact page.", 
      "comment_plain": "Web page type: Contact page.", 
      "id": "ContactPage", 
      "label": "Contact Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/ContactPage"
    }, 
    "ContactPoint": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A contact point\u2014for example, a Customer Complaints department.", 
      "comment_plain": "A contact point\u2014for example, a Customer Complaints department.", 
      "id": "ContactPoint", 
      "label": "Contact Point", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "contactType", 
        "email", 
        "faxNumber", 
        "telephone"
      ], 
      "specific_properties": [
        "contactType", 
        "email", 
        "faxNumber", 
        "telephone"
      ], 
      "subtypes": [
        "PostalAddress"
      ], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/ContactPoint"
    }, 
    "Continent": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform"
      ], 
      "comment": "One of the continents (for example, Europe or Africa).", 
      "comment_plain": "One of the continents (for example, Europe or Africa).", 
      "id": "Continent", 
      "label": "Continent", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Landform"
      ], 
      "url": "http://schema.org/Continent"
    }, 
    "ConvenienceStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A convenience store.", 
      "comment_plain": "A convenience store.", 
      "id": "ConvenienceStore", 
      "label": "Convenience Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ConvenienceStore"
    }, 
    "Corporation": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "Organization: A business corporation.", 
      "comment_plain": "Organization: A business corporation.", 
      "id": "Corporation", 
      "label": "Corporation", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "tickerSymbol"
      ], 
      "specific_properties": [
        "tickerSymbol"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/Corporation"
    }, 
    "Country": {
      "ancestors": [
        "Thing", 
        "Place", 
        "AdministrativeArea"
      ], 
      "comment": "A country.", 
      "comment_plain": "A country.", 
      "id": "Country", 
      "label": "Country", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AdministrativeArea"
      ], 
      "url": "http://schema.org/Country"
    }, 
    "Courthouse": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "GovernmentBuilding"
      ], 
      "comment": "A courthouse.", 
      "comment_plain": "A courthouse.", 
      "id": "Courthouse", 
      "label": "Courthouse", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentBuilding"
      ], 
      "url": "http://schema.org/Courthouse"
    }, 
    "CreativeWork": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "The most generic kind of creative work, including books, movies, photographs, software programs, etc.", 
      "comment_plain": "The most generic kind of creative work, including books, movies, photographs, software programs, etc.", 
      "id": "CreativeWork", 
      "label": "Creative Work", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "subtypes": [
        "Article", 
        "Blog", 
        "Book", 
        "Code", 
        "Comment", 
        "DataCatalog", 
        "Dataset", 
        "Diet", 
        "ExercisePlan", 
        "ItemList", 
        "Map", 
        "MediaObject", 
        "Movie", 
        "MusicPlaylist", 
        "MusicRecording", 
        "Painting", 
        "Photograph", 
        "Recipe", 
        "Review", 
        "Sculpture", 
        "SoftwareApplication", 
        "TVEpisode", 
        "TVSeason", 
        "TVSeries", 
        "WebPage", 
        "WebPageElement"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/CreativeWork"
    }, 
    "CreditCard": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration", 
        "PaymentMethod"
      ], 
      "comment": "A credit or debit card type as a standardized procedure for transferring the monetary amount for a purchase.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#AmericanExpress\nhttp://purl.org/goodrelations/v1#DinersClub\nhttp://purl.org/goodrelations/v1#Discover\nhttp://purl.org/goodrelations/v1#JCB\nhttp://purl.org/goodrelations/v1#MasterCard\nhttp://purl.org/goodrelations/v1#VISA", 
      "comment_plain": "A credit or debit card type as a standardized procedure for transferring the monetary amount for a purchase.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#AmericanExpress\nhttp://purl.org/goodrelations/v1#DinersClub\nhttp://purl.org/goodrelations/v1#Discover\nhttp://purl.org/goodrelations/v1#JCB\nhttp://purl.org/goodrelations/v1#MasterCard\nhttp://purl.org/goodrelations/v1#VISA", 
      "id": "CreditCard", 
      "label": "Credit Card", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PaymentMethod"
      ], 
      "url": "http://schema.org/CreditCard"
    }, 
    "Crematorium": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A crematorium.", 
      "comment_plain": "A crematorium.", 
      "id": "Crematorium", 
      "label": "Crematorium", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Crematorium"
    }, 
    "DDxElement": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.", 
      "comment_plain": "An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.", 
      "id": "DDxElement", 
      "label": "D Dx Element", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "diagnosis", 
        "distinguishingSign"
      ], 
      "specific_properties": [
        "diagnosis", 
        "distinguishingSign"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/DDxElement"
    }, 
    "DanceEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: A social dance.", 
      "comment_plain": "Event type: A social dance.", 
      "id": "DanceEvent", 
      "label": "Dance Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/DanceEvent"
    }, 
    "DanceGroup": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "PerformingGroup"
      ], 
      "comment": "A dance group\u2014for example, the Alvin Ailey Dance Theater or Riverdance.", 
      "comment_plain": "A dance group\u2014for example, the Alvin Ailey Dance Theater or Riverdance.", 
      "id": "DanceGroup", 
      "label": "Dance Group", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PerformingGroup"
      ], 
      "url": "http://schema.org/DanceGroup"
    }, 
    "DataCatalog": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A collection of datasets.", 
      "comment_plain": "A collection of datasets.", 
      "id": "DataCatalog", 
      "label": "Data Catalog", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "dataset"
      ], 
      "specific_properties": [
        "dataset"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/DataCatalog"
    }, 
    "DataDownload": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MediaObject"
      ], 
      "comment": "A dataset in downloadable form.", 
      "comment_plain": "A dataset in downloadable form.", 
      "id": "DataDownload", 
      "label": "Data Download", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MediaObject"
      ], 
      "url": "http://schema.org/DataDownload"
    }, 
    "Dataset": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A body of structured information describing some topic(s) of interest.", 
      "comment_plain": "A body of structured information describing some topic(s) of interest.", 
      "id": "Dataset", 
      "label": "Dataset", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "catalog", 
        "distribution", 
        "spatial", 
        "temporal"
      ], 
      "specific_properties": [
        "catalog", 
        "distribution", 
        "spatial", 
        "temporal"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Dataset"
    }, 
    "DayOfWeek": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Monday\nhttp://purl.org/goodrelations/v1#Tuesday\nhttp://purl.org/goodrelations/v1#Wednesday\nhttp://purl.org/goodrelations/v1#Thursday\nhttp://purl.org/goodrelations/v1#Friday\nhttp://purl.org/goodrelations/v1#Saturday\nhttp://purl.org/goodrelations/v1#Sunday\nhttp://purl.org/goodrelations/v1#PublicHolidays", 
      "comment_plain": "The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Monday\nhttp://purl.org/goodrelations/v1#Tuesday\nhttp://purl.org/goodrelations/v1#Wednesday\nhttp://purl.org/goodrelations/v1#Thursday\nhttp://purl.org/goodrelations/v1#Friday\nhttp://purl.org/goodrelations/v1#Saturday\nhttp://purl.org/goodrelations/v1#Sunday\nhttp://purl.org/goodrelations/v1#PublicHolidays", 
      "id": "DayOfWeek", 
      "label": "Day of Week", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/DayOfWeek"
    }, 
    "DaySpa": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "A day spa.", 
      "comment_plain": "A day spa.", 
      "id": "DaySpa", 
      "label": "Day Spa", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness"
      ], 
      "url": "http://schema.org/DaySpa"
    }, 
    "DefenceEstablishment": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "GovernmentBuilding"
      ], 
      "comment": "A defence establishment, such as an army or navy base.", 
      "comment_plain": "A defence establishment, such as an army or navy base.", 
      "id": "DefenceEstablishment", 
      "label": "Defence Establishment", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentBuilding"
      ], 
      "url": "http://schema.org/DefenceEstablishment"
    }, 
    "DeliveryChargeSpecification": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue", 
        "PriceSpecification"
      ], 
      "comment": "The price for the delivery of an offer using a particular delivery method.", 
      "comment_plain": "The price for the delivery of an offer using a particular delivery method.", 
      "id": "DeliveryChargeSpecification", 
      "label": "Delivery Charge Specification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "eligibleQuantity", 
        "eligibleTransactionVolume", 
        "maxPrice", 
        "minPrice", 
        "price", 
        "priceCurrency", 
        "validFrom", 
        "validThrough", 
        "valueAddedTaxIncluded", 
        "appliesToDeliveryMethod", 
        "eligibleRegion"
      ], 
      "specific_properties": [
        "appliesToDeliveryMethod", 
        "eligibleRegion"
      ], 
      "subtypes": [], 
      "supertypes": [
        "PriceSpecification"
      ], 
      "url": "http://schema.org/DeliveryChargeSpecification"
    }, 
    "DeliveryMethod": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A delivery method is a standardized procedure for transferring the product or service to the destination of fulfilment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#DeliveryModeDirectDownload\nhttp://purl.org/goodrelations/v1#DeliveryModeFreight\nhttp://purl.org/goodrelations/v1#DeliveryModeMail\nhttp://purl.org/goodrelations/v1#DeliveryModeOwnFleet\nhttp://purl.org/goodrelations/v1#DeliveryModePickUp\nhttp://purl.org/goodrelations/v1#DHL\nhttp://purl.org/goodrelations/v1#FederalExpress\nhttp://purl.org/goodrelations/v1#UPS", 
      "comment_plain": "A delivery method is a standardized procedure for transferring the product or service to the destination of fulfilment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#DeliveryModeDirectDownload\nhttp://purl.org/goodrelations/v1#DeliveryModeFreight\nhttp://purl.org/goodrelations/v1#DeliveryModeMail\nhttp://purl.org/goodrelations/v1#DeliveryModeOwnFleet\nhttp://purl.org/goodrelations/v1#DeliveryModePickUp\nhttp://purl.org/goodrelations/v1#DHL\nhttp://purl.org/goodrelations/v1#FederalExpress\nhttp://purl.org/goodrelations/v1#UPS", 
      "id": "DeliveryMethod", 
      "label": "Delivery Method", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "ParcelService"
      ], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/DeliveryMethod"
    }, 
    "Demand": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.", 
      "comment_plain": "A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.", 
      "id": "Demand", 
      "label": "Demand", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "acceptedPaymentMethod", 
        "advanceBookingRequirement", 
        "availability", 
        "availabilityEnds", 
        "availabilityStarts", 
        "availableAtOrFrom", 
        "availableDeliveryMethod", 
        "businessFunction", 
        "deliveryLeadTime", 
        "eligibleCustomerType", 
        "eligibleDuration", 
        "eligibleQuantity", 
        "eligibleRegion", 
        "eligibleTransactionVolume", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "includesObject", 
        "inventoryLevel", 
        "itemCondition", 
        "itemOffered", 
        "mpn", 
        "priceSpecification", 
        "seller", 
        "serialNumber", 
        "sku", 
        "validFrom", 
        "validThrough", 
        "warranty"
      ], 
      "specific_properties": [
        "acceptedPaymentMethod", 
        "advanceBookingRequirement", 
        "availability", 
        "availabilityEnds", 
        "availabilityStarts", 
        "availableAtOrFrom", 
        "availableDeliveryMethod", 
        "businessFunction", 
        "deliveryLeadTime", 
        "eligibleCustomerType", 
        "eligibleDuration", 
        "eligibleQuantity", 
        "eligibleRegion", 
        "eligibleTransactionVolume", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "includesObject", 
        "inventoryLevel", 
        "itemCondition", 
        "itemOffered", 
        "mpn", 
        "priceSpecification", 
        "seller", 
        "serialNumber", 
        "sku", 
        "validFrom", 
        "validThrough", 
        "warranty"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Demand"
    }, 
    "Dentist": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A dentist.", 
      "comment_plain": "A dentist.", 
      "id": "Dentist", 
      "label": "Dentist", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization", 
        "ProfessionalService"
      ], 
      "url": "http://schema.org/Dentist"
    }, 
    "DepartmentStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A department store.", 
      "comment_plain": "A department store.", 
      "id": "DepartmentStore", 
      "label": "Department Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/DepartmentStore"
    }, 
    "DiagnosticLab": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A medical laboratory that offers on-site or off-site diagnostic services.", 
      "comment_plain": "A medical laboratory that offers on-site or off-site diagnostic services.", 
      "id": "DiagnosticLab", 
      "label": "Diagnostic Lab", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "availableTest"
      ], 
      "specific_properties": [
        "availableTest"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/DiagnosticLab"
    }, 
    "DiagnosticProcedure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalProcedure"
      ], 
      "comment": "A medical procedure intended primarly for diagnostic, as opposed to therapeutic, purposes.", 
      "comment_plain": "A medical procedure intended primarly for diagnostic, as opposed to therapeutic, purposes.", 
      "id": "DiagnosticProcedure", 
      "label": "Diagnostic Procedure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice", 
        "followup", 
        "howPerformed", 
        "preparation", 
        "procedureType"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalProcedure", 
        "MedicalTest"
      ], 
      "url": "http://schema.org/DiagnosticProcedure"
    }, 
    "Diet": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.", 
      "comment_plain": "A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.", 
      "id": "Diet", 
      "label": "Diet", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "dietFeatures", 
        "endorsers", 
        "expertConsiderations", 
        "overview", 
        "physiologicalBenefits", 
        "proprietaryName", 
        "risks"
      ], 
      "specific_properties": [
        "dietFeatures", 
        "endorsers", 
        "expertConsiderations", 
        "overview", 
        "physiologicalBenefits", 
        "proprietaryName", 
        "risks"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork", 
        "LifestyleModification"
      ], 
      "url": "http://schema.org/Diet"
    }, 
    "DietarySupplement": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.", 
      "comment_plain": "A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.", 
      "id": "DietarySupplement", 
      "label": "Dietary Supplement", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "activeIngredient", 
        "background", 
        "dosageForm", 
        "isProprietary", 
        "legalStatus", 
        "manufacturer", 
        "maximumIntake", 
        "mechanismOfAction", 
        "nonProprietaryName", 
        "recommendedIntake", 
        "safetyConsideration", 
        "targetPopulation"
      ], 
      "specific_properties": [
        "activeIngredient", 
        "background", 
        "dosageForm", 
        "isProprietary", 
        "legalStatus", 
        "manufacturer", 
        "maximumIntake", 
        "mechanismOfAction", 
        "nonProprietaryName", 
        "recommendedIntake", 
        "safetyConsideration", 
        "targetPopulation"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/DietarySupplement"
    }, 
    "Distance": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Quantity"
      ], 
      "comment": "Properties that take Distances as values are of the form '<Number> <Length unit of measure>'. E.g., '7 ft'", 
      "comment_plain": "Properties that take Distances as values are of the form '<Number> <Length unit of measure>'. E.g., '7 ft'", 
      "id": "Distance", 
      "label": "Distance", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Quantity"
      ], 
      "url": "http://schema.org/Distance"
    }, 
    "DoseSchedule": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "A specific dosing schedule for a drug or supplement.", 
      "comment_plain": "A specific dosing schedule for a drug or supplement.", 
      "id": "DoseSchedule", 
      "label": "Dose Schedule", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "doseUnit", 
        "doseValue", 
        "frequency", 
        "targetPopulation"
      ], 
      "specific_properties": [
        "doseUnit", 
        "doseValue", 
        "frequency", 
        "targetPopulation"
      ], 
      "subtypes": [
        "MaximumDoseSchedule", 
        "RecommendedDoseSchedule", 
        "ReportedDoseSchedule"
      ], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/DoseSchedule"
    }, 
    "Drug": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism.", 
      "comment_plain": "A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism.", 
      "id": "Drug", 
      "label": "Drug", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "activeIngredient", 
        "administrationRoute", 
        "alcoholWarning", 
        "availableStrength", 
        "breastfeedingWarning", 
        "clincalPharmacology", 
        "cost", 
        "dosageForm", 
        "doseSchedule", 
        "drugClass", 
        "foodWarning", 
        "interactingDrug", 
        "isAvailableGenerically", 
        "isProprietary", 
        "labelDetails", 
        "legalStatus", 
        "manufacturer", 
        "mechanismOfAction", 
        "nonProprietaryName", 
        "overdosage", 
        "pregnancyCategory", 
        "pregnancyWarning", 
        "prescribingInfo", 
        "prescriptionStatus", 
        "relatedDrug", 
        "warning"
      ], 
      "specific_properties": [
        "activeIngredient", 
        "administrationRoute", 
        "alcoholWarning", 
        "availableStrength", 
        "breastfeedingWarning", 
        "clincalPharmacology", 
        "cost", 
        "dosageForm", 
        "doseSchedule", 
        "drugClass", 
        "foodWarning", 
        "interactingDrug", 
        "isAvailableGenerically", 
        "isProprietary", 
        "labelDetails", 
        "legalStatus", 
        "manufacturer", 
        "mechanismOfAction", 
        "nonProprietaryName", 
        "overdosage", 
        "pregnancyCategory", 
        "pregnancyWarning", 
        "prescribingInfo", 
        "prescriptionStatus", 
        "relatedDrug", 
        "warning"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/Drug"
    }, 
    "DrugClass": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.", 
      "comment_plain": "A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.", 
      "id": "DrugClass", 
      "label": "Drug Class", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "drug"
      ], 
      "specific_properties": [
        "drug"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/DrugClass"
    }, 
    "DrugCost": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup.", 
      "comment_plain": "The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup.", 
      "id": "DrugCost", 
      "label": "Drug Cost", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "applicableLocation", 
        "costCategory", 
        "costCurrency", 
        "costOrigin", 
        "costPerUnit", 
        "drugUnit"
      ], 
      "specific_properties": [
        "applicableLocation", 
        "costCategory", 
        "costCurrency", 
        "costOrigin", 
        "costPerUnit", 
        "drugUnit"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/DrugCost"
    }, 
    "DrugCostCategory": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Enumerated categories of medical drug costs.", 
      "comment_plain": "Enumerated categories of medical drug costs.", 
      "id": "DrugCostCategory", 
      "instances": [
        "ReimbursementCap", 
        "Retail", 
        "Wholesale"
      ], 
      "label": "Drug Cost Category", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/DrugCostCategory"
    }, 
    "DrugLegalStatus": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "The legal availability status of a medical drug.", 
      "comment_plain": "The legal availability status of a medical drug.", 
      "id": "DrugLegalStatus", 
      "label": "Drug Legal Status", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "applicableLocation"
      ], 
      "specific_properties": [
        "applicableLocation"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/DrugLegalStatus"
    }, 
    "DrugPregnancyCategory": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.", 
      "comment_plain": "Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.", 
      "id": "DrugPregnancyCategory", 
      "instances": [
        "FDAcategoryA", 
        "FDAcategoryB", 
        "FDAcategoryC", 
        "FDAcategoryD", 
        "FDAcategoryX", 
        "FDAnotEvaluated"
      ], 
      "label": "Drug Pregnancy Category", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/DrugPregnancyCategory"
    }, 
    "DrugPrescriptionStatus": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Indicates whether this drug is available by prescription or over-the-counter.", 
      "comment_plain": "Indicates whether this drug is available by prescription or over-the-counter.", 
      "id": "DrugPrescriptionStatus", 
      "instances": [
        "OTC", 
        "PrescriptionOnly"
      ], 
      "label": "Drug Prescription Status", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/DrugPrescriptionStatus"
    }, 
    "DrugStrength": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "A specific strength in which a medical drug is available in a specific country.", 
      "comment_plain": "A specific strength in which a medical drug is available in a specific country.", 
      "id": "DrugStrength", 
      "label": "Drug Strength", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "activeIngredient", 
        "availableIn", 
        "strengthUnit", 
        "strengthValue"
      ], 
      "specific_properties": [
        "activeIngredient", 
        "availableIn", 
        "strengthUnit", 
        "strengthValue"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/DrugStrength"
    }, 
    "DryCleaningOrLaundry": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A dry-cleaning business.", 
      "comment_plain": "A dry-cleaning business.", 
      "id": "DryCleaningOrLaundry", 
      "label": "Dry Cleaning or Laundry", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/DryCleaningOrLaundry"
    }, 
    "Duration": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Quantity"
      ], 
      "comment": "Quantity: Duration (use  <a href=\"http://en.wikipedia.org/wiki/ISO_8601\">ISO 8601 duration format</a>).", 
      "comment_plain": "Quantity: Duration (use  ISO 8601 duration format).", 
      "id": "Duration", 
      "label": "Duration", 
      "properties": [], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Quantity"
      ], 
      "url": "http://schema.org/Duration"
    }, 
    "EducationEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Education event.", 
      "comment_plain": "Event type: Education event.", 
      "id": "EducationEvent", 
      "label": "Education Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/EducationEvent"
    }, 
    "EducationalAudience": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Audience"
      ], 
      "comment": "An EducationalAudience", 
      "comment_plain": "An EducationalAudience", 
      "id": "EducationalAudience", 
      "label": "Educational Audience", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "educationalRole"
      ], 
      "specific_properties": [
        "educationalRole"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Audience"
      ], 
      "url": "http://schema.org/EducationalAudience"
    }, 
    "EducationalOrganization": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "An educational organization.", 
      "comment_plain": "An educational organization.", 
      "id": "EducationalOrganization", 
      "label": "Educational Organization", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [
        "alumni"
      ], 
      "subtypes": [
        "CollegeOrUniversity", 
        "ElementarySchool", 
        "HighSchool", 
        "MiddleSchool", 
        "Preschool", 
        "School"
      ], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/EducationalOrganization"
    }, 
    "Electrician": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "An electrician.", 
      "comment_plain": "An electrician.", 
      "id": "Electrician", 
      "label": "Electrician", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/Electrician"
    }, 
    "ElectronicsStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "An electronics store.", 
      "comment_plain": "An electronics store.", 
      "id": "ElectronicsStore", 
      "label": "Electronics Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ElectronicsStore"
    }, 
    "ElementarySchool": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "An elementary school.", 
      "comment_plain": "An elementary school.", 
      "id": "ElementarySchool", 
      "label": "Elementary School", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/ElementarySchool"
    }, 
    "Embassy": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "GovernmentBuilding"
      ], 
      "comment": "An embassy.", 
      "comment_plain": "An embassy.", 
      "id": "Embassy", 
      "label": "Embassy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentBuilding"
      ], 
      "url": "http://schema.org/Embassy"
    }, 
    "EmergencyService": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "An emergency service, such as a fire station or ER.", 
      "comment_plain": "An emergency service, such as a fire station or ER.", 
      "id": "EmergencyService", 
      "label": "Emergency Service", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "FireStation", 
        "Hospital", 
        "PoliceStation"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/EmergencyService"
    }, 
    "EmploymentAgency": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "An employment agency.", 
      "comment_plain": "An employment agency.", 
      "id": "EmploymentAgency", 
      "label": "Employment Agency", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/EmploymentAgency"
    }, 
    "Energy": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Quantity"
      ], 
      "comment": "Properties that take Enerygy as values are of the form '<Number> <Energy unit of measure>'", 
      "comment_plain": "Properties that take Enerygy as values are of the form '<Number> <Energy unit of measure>'", 
      "id": "Energy", 
      "label": "Energy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Quantity"
      ], 
      "url": "http://schema.org/Energy"
    }, 
    "EntertainmentBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A business providing entertainment.", 
      "comment_plain": "A business providing entertainment.", 
      "id": "EntertainmentBusiness", 
      "label": "Entertainment Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AdultEntertainment", 
        "AmusementPark", 
        "ArtGallery", 
        "Casino", 
        "ComedyClub", 
        "MovieTheater", 
        "NightClub"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/EntertainmentBusiness"
    }, 
    "Enumeration": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "Lists or enumerations\u2014for example, a list of cuisines or music genres, etc.", 
      "comment_plain": "Lists or enumerations\u2014for example, a list of cuisines or music genres, etc.", 
      "id": "Enumeration", 
      "label": "Enumeration", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BookFormatType", 
        "BusinessEntityType", 
        "BusinessFunction", 
        "DayOfWeek", 
        "DeliveryMethod", 
        "ItemAvailability", 
        "OfferItemCondition", 
        "PaymentMethod", 
        "QualitativeValue", 
        "Specialty", 
        "WarrantyScope"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Enumeration"
    }, 
    "Event": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "An event happening at a certain time at a certain location.", 
      "comment_plain": "An event happening at a certain time at a certain location.", 
      "id": "Event", 
      "label": "Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "subtypes": [
        "BusinessEvent", 
        "ChildrensEvent", 
        "ComedyEvent", 
        "DanceEvent", 
        "EducationEvent", 
        "Festival", 
        "FoodEvent", 
        "LiteraryEvent", 
        "MusicEvent", 
        "SaleEvent", 
        "SocialEvent", 
        "SportsEvent", 
        "TheaterEvent", 
        "UserInteraction", 
        "VisualArtsEvent"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Event"
    }, 
    "EventVenue": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "An event venue.", 
      "comment_plain": "An event venue.", 
      "id": "EventVenue", 
      "label": "Event Venue", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/EventVenue"
    }, 
    "ExerciseGym": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A gym.", 
      "comment_plain": "A gym.", 
      "id": "ExerciseGym", 
      "label": "Exercise Gym", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/ExerciseGym"
    }, 
    "ExercisePlan": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.", 
      "comment_plain": "Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.", 
      "id": "ExercisePlan", 
      "label": "Exercise Plan", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "associatedAnatomy", 
        "category", 
        "epidemiology", 
        "pathophysiology", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "activityDuration", 
        "activityFrequency", 
        "additionalVariable", 
        "exerciseType", 
        "intensity", 
        "repetitions", 
        "restPeriods", 
        "workload"
      ], 
      "specific_properties": [
        "activityDuration", 
        "activityFrequency", 
        "additionalVariable", 
        "exerciseType", 
        "intensity", 
        "repetitions", 
        "restPeriods", 
        "workload"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork", 
        "PhysicalActivity"
      ], 
      "url": "http://schema.org/ExercisePlan"
    }, 
    "FastFoodRestaurant": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A fast-food restaurant.", 
      "comment_plain": "A fast-food restaurant.", 
      "id": "FastFoodRestaurant", 
      "label": "Fast Food Restaurant", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/FastFoodRestaurant"
    }, 
    "Festival": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Festival.", 
      "comment_plain": "Event type: Festival.", 
      "id": "Festival", 
      "label": "Festival", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/Festival"
    }, 
    "FinancialService": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Financial services business.", 
      "comment_plain": "Financial services business.", 
      "id": "FinancialService", 
      "label": "Financial Service", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AccountingService", 
        "AutomatedTeller", 
        "BankOrCreditUnion", 
        "InsuranceAgency"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/FinancialService"
    }, 
    "FireStation": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A fire station. With firemen.", 
      "comment_plain": "A fire station. With firemen.", 
      "id": "FireStation", 
      "label": "Fire Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure", 
        "EmergencyService"
      ], 
      "url": "http://schema.org/FireStation"
    }, 
    "Florist": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A florist.", 
      "comment_plain": "A florist.", 
      "id": "Florist", 
      "label": "Florist", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/Florist"
    }, 
    "FoodEstablishment": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A food-related business.", 
      "comment_plain": "A food-related business.", 
      "id": "FoodEstablishment", 
      "label": "Food Establishment", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "subtypes": [
        "Bakery", 
        "BarOrPub", 
        "Brewery", 
        "CafeOrCoffeeShop", 
        "FastFoodRestaurant", 
        "IceCreamShop", 
        "Restaurant", 
        "Winery"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/FoodEstablishment"
    }, 
    "FoodEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Food event.", 
      "comment_plain": "Event type: Food event.", 
      "id": "FoodEvent", 
      "label": "Food Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/FoodEvent"
    }, 
    "FurnitureStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A furniture store.", 
      "comment_plain": "A furniture store.", 
      "id": "FurnitureStore", 
      "label": "Furniture Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/FurnitureStore"
    }, 
    "GardenStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A garden store.", 
      "comment_plain": "A garden store.", 
      "id": "GardenStore", 
      "label": "Garden Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/GardenStore"
    }, 
    "GasStation": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "A gas station.", 
      "comment_plain": "A gas station.", 
      "id": "GasStation", 
      "label": "Gas Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/GasStation"
    }, 
    "GatedResidenceCommunity": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Residence"
      ], 
      "comment": "Residence type: Gated community.", 
      "comment_plain": "Residence type: Gated community.", 
      "id": "GatedResidenceCommunity", 
      "label": "Gated Residence Community", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Residence"
      ], 
      "url": "http://schema.org/GatedResidenceCommunity"
    }, 
    "GeneralContractor": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A general contractor.", 
      "comment_plain": "A general contractor.", 
      "id": "GeneralContractor", 
      "label": "General Contractor", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/GeneralContractor"
    }, 
    "GeoCoordinates": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "The geographic coordinates of a place or event.", 
      "comment_plain": "The geographic coordinates of a place or event.", 
      "id": "GeoCoordinates", 
      "label": "Geo Coordinates", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "elevation", 
        "latitude", 
        "longitude"
      ], 
      "specific_properties": [
        "elevation", 
        "latitude", 
        "longitude"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/GeoCoordinates"
    }, 
    "GeoShape": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "The geographic shape of a place.", 
      "comment_plain": "The geographic shape of a place.", 
      "id": "GeoShape", 
      "label": "Geo Shape", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "box", 
        "circle", 
        "elevation", 
        "line", 
        "polygon"
      ], 
      "specific_properties": [
        "box", 
        "circle", 
        "elevation", 
        "line", 
        "polygon"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/GeoShape"
    }, 
    "GolfCourse": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A golf course.", 
      "comment_plain": "A golf course.", 
      "id": "GolfCourse", 
      "label": "Golf Course", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/GolfCourse"
    }, 
    "GovernmentBuilding": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A government building.", 
      "comment_plain": "A government building.", 
      "id": "GovernmentBuilding", 
      "label": "Government Building", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "CityHall", 
        "Courthouse", 
        "DefenceEstablishment", 
        "Embassy", 
        "LegislativeBuilding"
      ], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/GovernmentBuilding"
    }, 
    "GovernmentOffice": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A government office\u2014for example, an IRS or DMV office.", 
      "comment_plain": "A government office\u2014for example, an IRS or DMV office.", 
      "id": "GovernmentOffice", 
      "label": "Government Office", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "PostOffice"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/GovernmentOffice"
    }, 
    "GovernmentOrganization": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "A governmental organization or agency.", 
      "comment_plain": "A governmental organization or agency.", 
      "id": "GovernmentOrganization", 
      "label": "Government Organization", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/GovernmentOrganization"
    }, 
    "GroceryStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A grocery store.", 
      "comment_plain": "A grocery store.", 
      "id": "GroceryStore", 
      "label": "Grocery Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/GroceryStore"
    }, 
    "HVACBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "An HVAC service.", 
      "comment_plain": "An HVAC service.", 
      "id": "HVACBusiness", 
      "label": "HVAC Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/HVACBusiness"
    }, 
    "HairSalon": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "A hair salon.", 
      "comment_plain": "A hair salon.", 
      "id": "HairSalon", 
      "label": "Hair Salon", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness"
      ], 
      "url": "http://schema.org/HairSalon"
    }, 
    "HardwareStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A hardware store.", 
      "comment_plain": "A hardware store.", 
      "id": "HardwareStore", 
      "label": "Hardware Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/HardwareStore"
    }, 
    "HealthAndBeautyBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Health and beauty.", 
      "comment_plain": "Health and beauty.", 
      "id": "HealthAndBeautyBusiness", 
      "label": "Health And Beauty Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BeautySalon", 
        "DaySpa", 
        "HairSalon", 
        "HealthClub", 
        "NailSalon", 
        "TattooParlor"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/HealthAndBeautyBusiness"
    }, 
    "HealthClub": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "A health club.", 
      "comment_plain": "A health club.", 
      "id": "HealthClub", 
      "label": "Health Club", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness", 
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/HealthClub"
    }, 
    "HighSchool": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "A high school.", 
      "comment_plain": "A high school.", 
      "id": "HighSchool", 
      "label": "High School", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/HighSchool"
    }, 
    "HinduTemple": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A Hindu temple.", 
      "comment_plain": "A Hindu temple.", 
      "id": "HinduTemple", 
      "label": "Hindu Temple", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/HinduTemple"
    }, 
    "HobbyShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A hobby store.", 
      "comment_plain": "A hobby store.", 
      "id": "HobbyShop", 
      "label": "Hobby Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/HobbyShop"
    }, 
    "HomeAndConstructionBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A construction business.", 
      "comment_plain": "A construction business.", 
      "id": "HomeAndConstructionBusiness", 
      "label": "Home And Construction Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Electrician", 
        "GeneralContractor", 
        "HVACBusiness", 
        "HousePainter", 
        "Locksmith", 
        "MovingCompany", 
        "Plumber", 
        "RoofingContractor"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/HomeAndConstructionBusiness"
    }, 
    "HomeGoodsStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A home goods store.", 
      "comment_plain": "A home goods store.", 
      "id": "HomeGoodsStore", 
      "label": "Home Goods Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/HomeGoodsStore"
    }, 
    "Hospital": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A hospital.", 
      "comment_plain": "A hospital.", 
      "id": "Hospital", 
      "label": "Hospital", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "availableService", 
        "medicalSpecialty"
      ], 
      "specific_properties": [
        "availableService", 
        "medicalSpecialty"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure", 
        "MedicalOrganization", 
        "EmergencyService"
      ], 
      "url": "http://schema.org/Hospital"
    }, 
    "Hostel": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "LodgingBusiness"
      ], 
      "comment": "A hostel.", 
      "comment_plain": "A hostel.", 
      "id": "Hostel", 
      "label": "Hostel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LodgingBusiness"
      ], 
      "url": "http://schema.org/Hostel"
    }, 
    "Hotel": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "LodgingBusiness"
      ], 
      "comment": "A hotel.", 
      "comment_plain": "A hotel.", 
      "id": "Hotel", 
      "label": "Hotel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LodgingBusiness"
      ], 
      "url": "http://schema.org/Hotel"
    }, 
    "HousePainter": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A house painting service.", 
      "comment_plain": "A house painting service.", 
      "id": "HousePainter", 
      "label": "House Painter", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/HousePainter"
    }, 
    "IceCreamShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "An ice cream shop", 
      "comment_plain": "An ice cream shop", 
      "id": "IceCreamShop", 
      "label": "Ice Cream Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/IceCreamShop"
    }, 
    "ImageGallery": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage", 
        "CollectionPage"
      ], 
      "comment": "Web page type: Image gallery page.", 
      "comment_plain": "Web page type: Image gallery page.", 
      "id": "ImageGallery", 
      "label": "Image Gallery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CollectionPage"
      ], 
      "url": "http://schema.org/ImageGallery"
    }, 
    "ImageObject": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MediaObject"
      ], 
      "comment": "An image file.", 
      "comment_plain": "An image file.", 
      "id": "ImageObject", 
      "label": "Image Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width", 
        "caption", 
        "exifData", 
        "representativeOfPage", 
        "thumbnail"
      ], 
      "specific_properties": [
        "caption", 
        "exifData", 
        "representativeOfPage", 
        "thumbnail"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MediaObject"
      ], 
      "url": "http://schema.org/ImageObject"
    }, 
    "ImagingTest": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTest"
      ], 
      "comment": "Any medical imaging modality typically used for diagnostic purposes.", 
      "comment_plain": "Any medical imaging modality typically used for diagnostic purposes.", 
      "id": "ImagingTest", 
      "label": "Imaging Test", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice", 
        "imagingTechnique"
      ], 
      "specific_properties": [
        "imagingTechnique"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTest"
      ], 
      "url": "http://schema.org/ImagingTest"
    }, 
    "IndividualProduct": {
      "ancestors": [
        "Thing", 
        "Product"
      ], 
      "comment": "A single, identifiable product instance (e.g. a laptop with a particular serial number).", 
      "comment_plain": "A single, identifiable product instance (e.g. a laptop with a particular serial number).", 
      "id": "IndividualProduct", 
      "label": "Individual Product", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "aggregateRating", 
        "audience", 
        "brand", 
        "color", 
        "depth", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "height", 
        "isAccessoryOrSparePartFor", 
        "isConsumableFor", 
        "isRelatedTo", 
        "isSimilarTo", 
        "itemCondition", 
        "logo", 
        "manufacturer", 
        "model", 
        "mpn", 
        "offers", 
        "productID", 
        "releaseDate", 
        "review", 
        "reviews", 
        "sku", 
        "weight", 
        "width", 
        "serialNumber"
      ], 
      "specific_properties": [
        "serialNumber"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Product"
      ], 
      "url": "http://schema.org/IndividualProduct"
    }, 
    "InfectiousAgentClass": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Classes of agents or pathogens that transmit infectious diseases. Enumerated type.", 
      "comment_plain": "Classes of agents or pathogens that transmit infectious diseases. Enumerated type.", 
      "id": "InfectiousAgentClass", 
      "instances": [
        "Bacteria", 
        "Fungus", 
        "MulticellularParasite", 
        "Prion", 
        "Protozoa", 
        "Virus"
      ], 
      "label": "Infectious Agent Class", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/InfectiousAgentClass"
    }, 
    "InfectiousDisease": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalCondition"
      ], 
      "comment": "An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.", 
      "comment_plain": "An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.", 
      "id": "InfectiousDisease", 
      "label": "Infectious Disease", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedAnatomy", 
        "cause", 
        "differentialDiagnosis", 
        "epidemiology", 
        "expectedPrognosis", 
        "naturalProgression", 
        "pathophysiology", 
        "possibleComplication", 
        "possibleTreatment", 
        "primaryPrevention", 
        "riskFactor", 
        "secondaryPrevention", 
        "signOrSymptom", 
        "stage", 
        "subtype", 
        "typicalTest", 
        "infectiousAgent", 
        "infectiousAgentClass", 
        "transmissionMethod"
      ], 
      "specific_properties": [
        "infectiousAgent", 
        "infectiousAgentClass", 
        "transmissionMethod"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalCondition"
      ], 
      "url": "http://schema.org/InfectiousDisease"
    }, 
    "InsuranceAgency": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FinancialService"
      ], 
      "comment": "Insurance agency.", 
      "comment_plain": "Insurance agency.", 
      "id": "InsuranceAgency", 
      "label": "Insurance Agency", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FinancialService"
      ], 
      "url": "http://schema.org/InsuranceAgency"
    }, 
    "Intangible": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.", 
      "comment_plain": "A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.", 
      "id": "Intangible", 
      "label": "Intangible", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AlignmentObject", 
        "Audience", 
        "Brand", 
        "Demand", 
        "Enumeration", 
        "JobPosting", 
        "Language", 
        "Offer", 
        "Quantity", 
        "Rating", 
        "StructuredValue"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Intangible"
    }, 
    "InternetCafe": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "An internet cafe.", 
      "comment_plain": "An internet cafe.", 
      "id": "InternetCafe", 
      "label": "Internet Cafe", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/InternetCafe"
    }, 
    "ItemAvailability": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A list of possible product availablity options.", 
      "comment_plain": "A list of possible product availablity options.", 
      "id": "ItemAvailability", 
      "instances": [
        "Discontinued", 
        "InStock", 
        "InStoreOnly", 
        "OnlineOnly", 
        "OutOfStock", 
        "PreOrder"
      ], 
      "label": "Item Availability", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/ItemAvailability"
    }, 
    "ItemList": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A list of items of any sort\u2014for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.", 
      "comment_plain": "A list of items of any sort\u2014for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.", 
      "id": "ItemList", 
      "label": "Item List", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "itemListElement", 
        "itemListOrder"
      ], 
      "specific_properties": [
        "itemListElement", 
        "itemListOrder"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/ItemList"
    }, 
    "ItemPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "A page devoted to a single item, such as a particular product or hotel.", 
      "comment_plain": "A page devoted to a single item, such as a particular product or hotel.", 
      "id": "ItemPage", 
      "label": "Item Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/ItemPage"
    }, 
    "JewelryStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A jewelry store.", 
      "comment_plain": "A jewelry store.", 
      "id": "JewelryStore", 
      "label": "Jewelry Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/JewelryStore"
    }, 
    "JobPosting": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "A listing that describes a job opening in a certain organization.", 
      "comment_plain": "A listing that describes a job opening in a certain organization.", 
      "id": "JobPosting", 
      "label": "Job Posting", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "baseSalary", 
        "benefits", 
        "datePosted", 
        "educationRequirements", 
        "employmentType", 
        "experienceRequirements", 
        "hiringOrganization", 
        "incentives", 
        "industry", 
        "jobLocation", 
        "occupationalCategory", 
        "qualifications", 
        "responsibilities", 
        "salaryCurrency", 
        "skills", 
        "specialCommitments", 
        "title", 
        "workHours"
      ], 
      "specific_properties": [
        "baseSalary", 
        "benefits", 
        "datePosted", 
        "educationRequirements", 
        "employmentType", 
        "experienceRequirements", 
        "hiringOrganization", 
        "incentives", 
        "industry", 
        "jobLocation", 
        "occupationalCategory", 
        "qualifications", 
        "responsibilities", 
        "salaryCurrency", 
        "skills", 
        "specialCommitments", 
        "title", 
        "workHours"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/JobPosting"
    }, 
    "Joint": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "The anatomical location at which two or more bones make contact.", 
      "comment_plain": "The anatomical location at which two or more bones make contact.", 
      "id": "Joint", 
      "label": "Joint", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "biomechnicalClass", 
        "functionalClass", 
        "structuralClass"
      ], 
      "specific_properties": [
        "biomechnicalClass", 
        "functionalClass", 
        "structuralClass"
      ], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Joint"
    }, 
    "LakeBodyOfWater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A lake (for example, Lake Pontrachain).", 
      "comment_plain": "A lake (for example, Lake Pontrachain).", 
      "id": "LakeBodyOfWater", 
      "label": "Lake Body of Water", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/LakeBodyOfWater"
    }, 
    "Landform": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.", 
      "comment_plain": "A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.", 
      "id": "Landform", 
      "label": "Landform", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BodyOfWater", 
        "Continent", 
        "Mountain", 
        "Volcano"
      ], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/Landform"
    }, 
    "LandmarksOrHistoricalBuildings": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "An historical landmark or building.", 
      "comment_plain": "An historical landmark or building.", 
      "id": "LandmarksOrHistoricalBuildings", 
      "label": "Landmarks or Historical Buildings", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/LandmarksOrHistoricalBuildings"
    }, 
    "Language": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "Natural languages such as Spanish, Tamil, Hindi, English, etc. and programming languages such as Scheme and Lisp.", 
      "comment_plain": "Natural languages such as Spanish, Tamil, Hindi, English, etc. and programming languages such as Scheme and Lisp.", 
      "id": "Language", 
      "label": "Language", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Language"
    }, 
    "LegislativeBuilding": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "GovernmentBuilding"
      ], 
      "comment": "A legislative building\u2014for example, the state capitol.", 
      "comment_plain": "A legislative building\u2014for example, the state capitol.", 
      "id": "LegislativeBuilding", 
      "label": "Legislative Building", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentBuilding"
      ], 
      "url": "http://schema.org/LegislativeBuilding"
    }, 
    "Library": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A library.", 
      "comment_plain": "A library.", 
      "id": "Library", 
      "label": "Library", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/Library"
    }, 
    "LifestyleModification": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.", 
      "comment_plain": "A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.", 
      "id": "LifestyleModification", 
      "label": "Lifestyle Modification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Diet", 
        "PhysicalActivity"
      ], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/LifestyleModification"
    }, 
    "Ligament": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.", 
      "comment_plain": "A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.", 
      "id": "Ligament", 
      "label": "Ligament", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Ligament"
    }, 
    "LiquorStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A liquor store.", 
      "comment_plain": "A liquor store.", 
      "id": "LiquorStore", 
      "label": "Liquor Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/LiquorStore"
    }, 
    "LiteraryEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Literary event.", 
      "comment_plain": "Event type: Literary event.", 
      "id": "LiteraryEvent", 
      "label": "Literary Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/LiteraryEvent"
    }, 
    "LocalBusiness": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.", 
      "comment_plain": "A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.", 
      "id": "LocalBusiness", 
      "label": "Local Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "subtypes": [
        "AnimalShelter", 
        "AutomotiveBusiness", 
        "ChildCare", 
        "DryCleaningOrLaundry", 
        "EmergencyService", 
        "EmploymentAgency", 
        "EntertainmentBusiness", 
        "FinancialService", 
        "FoodEstablishment", 
        "GovernmentOffice", 
        "HealthAndBeautyBusiness", 
        "HomeAndConstructionBusiness", 
        "InternetCafe", 
        "Library", 
        "LodgingBusiness", 
        "MedicalOrganization", 
        "ProfessionalService", 
        "RadioStation", 
        "RealEstateAgent", 
        "RecyclingCenter", 
        "SelfStorage", 
        "ShoppingCenter", 
        "SportsActivityLocation", 
        "Store", 
        "TelevisionStation", 
        "TouristInformationCenter", 
        "TravelAgency"
      ], 
      "supertypes": [
        "Organization", 
        "Place"
      ], 
      "url": "http://schema.org/LocalBusiness"
    }, 
    "Locksmith": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A locksmith.", 
      "comment_plain": "A locksmith.", 
      "id": "Locksmith", 
      "label": "Locksmith", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/Locksmith"
    }, 
    "LodgingBusiness": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A lodging business, such as a motel, hotel, or inn.", 
      "comment_plain": "A lodging business, such as a motel, hotel, or inn.", 
      "id": "LodgingBusiness", 
      "label": "Lodging Business", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BedAndBreakfast", 
        "Hostel", 
        "Hotel", 
        "Motel"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/LodgingBusiness"
    }, 
    "LymphaticVessel": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure", 
        "Vessel"
      ], 
      "comment": "A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.", 
      "comment_plain": "A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.", 
      "id": "LymphaticVessel", 
      "label": "Lymphatic Vessel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "originatesFrom", 
        "regionDrained", 
        "runsTo"
      ], 
      "specific_properties": [
        "originatesFrom", 
        "regionDrained", 
        "runsTo"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Vessel"
      ], 
      "url": "http://schema.org/LymphaticVessel"
    }, 
    "Map": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A map.", 
      "comment_plain": "A map.", 
      "id": "Map", 
      "label": "Map", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Map"
    }, 
    "Mass": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Quantity"
      ], 
      "comment": "Properties that take Mass as values are of the form '<Number> <Mass unit of measure>'. E.g., '7 kg'", 
      "comment_plain": "Properties that take Mass as values are of the form '<Number> <Mass unit of measure>'. E.g., '7 kg'", 
      "id": "Mass", 
      "label": "Mass", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Quantity"
      ], 
      "url": "http://schema.org/Mass"
    }, 
    "MaximumDoseSchedule": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "DoseSchedule"
      ], 
      "comment": "The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.", 
      "comment_plain": "The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.", 
      "id": "MaximumDoseSchedule", 
      "label": "Maximum Dose Schedule", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "doseUnit", 
        "doseValue", 
        "frequency", 
        "targetPopulation"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DoseSchedule"
      ], 
      "url": "http://schema.org/MaximumDoseSchedule"
    }, 
    "MediaObject": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).", 
      "comment_plain": "An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).", 
      "id": "MediaObject", 
      "label": "Media Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width"
      ], 
      "specific_properties": [
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width"
      ], 
      "subtypes": [
        "AudioObject", 
        "DataDownload", 
        "ImageObject", 
        "MusicVideoObject", 
        "VideoObject"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/MediaObject"
    }, 
    "MedicalAudience": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Audience"
      ], 
      "comment": "Target audiences for medical web pages. Enumerated type.", 
      "comment_plain": "Target audiences for medical web pages. Enumerated type.", 
      "id": "MedicalAudience", 
      "instances": [
        "Clinician", 
        "MedicalResearcher", 
        "Patient"
      ], 
      "label": "Medical Audience", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "healthCondition", 
        "suggestedGender", 
        "suggestedMaxAge", 
        "suggestedMinAge", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PeopleAudience", 
        "Audience", 
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalAudience"
    }, 
    "MedicalCause": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "The causative agent(s) that are responsible for the pathophysiologic process that eventually results in a medical condition, symptom or sign. In this schema, unless otherwise specified this is meant to be the proximate cause of the medical condition, symptom or sign. The proximate cause is defined as the causative agent that most directly results in the medical condition, symptom or sign. For example, the HIV virus could be considered a cause of AIDS. Or in a diagnostic context, if a patient fell and sustained a hip fracture and two days later sustained a pulmonary embolism which eventuated in a cardiac arrest, the cause of the cardiac arrest (the proximate cause) would be the pulmonary embolism and not the fall. <p>Medical causes can include cardiovascular, chemical, dermatologic, endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic, iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric, oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal, rheumatologic, toxic, traumatic, or urologic causes; medical conditions can be causes as well.\n\n\n\n        </p>", 
      "comment_plain": "The causative agent(s) that are responsible for the pathophysiologic process that eventually results in a medical condition, symptom or sign. In this schema, unless otherwise specified this is meant to be the proximate cause of the medical condition, symptom or sign. The proximate cause is defined as the causative agent that most directly results in the medical condition, symptom or sign. For example, the HIV virus could be considered a cause of AIDS. Or in a diagnostic context, if a patient fell and sustained a hip fracture and two days later sustained a pulmonary embolism which eventuated in a cardiac arrest, the cause of the cardiac arrest (the proximate cause) would be the pulmonary embolism and not the fall. Medical causes can include cardiovascular, chemical, dermatologic, endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic, iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric, oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal, rheumatologic, toxic, traumatic, or urologic causes; medical conditions can be causes as well.", 
      "id": "MedicalCause", 
      "label": "Medical Cause", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "causeOf"
      ], 
      "specific_properties": [
        "causeOf"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalCause"
    }, 
    "MedicalClinic": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A medical clinic.", 
      "comment_plain": "A medical clinic.", 
      "id": "MedicalClinic", 
      "label": "Medical Clinic", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "availableService", 
        "medicalSpecialty"
      ], 
      "specific_properties": [
        "availableService", 
        "medicalSpecialty"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/MedicalClinic"
    }, 
    "MedicalCode": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "A code for a medical entity.", 
      "comment_plain": "A code for a medical entity.", 
      "id": "MedicalCode", 
      "label": "Medical Code", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "codeValue", 
        "codingSystem"
      ], 
      "specific_properties": [
        "codeValue", 
        "codingSystem"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/MedicalCode"
    }, 
    "MedicalCondition": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.", 
      "comment_plain": "Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.", 
      "id": "MedicalCondition", 
      "label": "Medical Condition", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedAnatomy", 
        "cause", 
        "differentialDiagnosis", 
        "epidemiology", 
        "expectedPrognosis", 
        "naturalProgression", 
        "pathophysiology", 
        "possibleComplication", 
        "possibleTreatment", 
        "primaryPrevention", 
        "riskFactor", 
        "secondaryPrevention", 
        "signOrSymptom", 
        "stage", 
        "subtype", 
        "typicalTest"
      ], 
      "specific_properties": [
        "associatedAnatomy", 
        "cause", 
        "differentialDiagnosis", 
        "epidemiology", 
        "expectedPrognosis", 
        "naturalProgression", 
        "pathophysiology", 
        "possibleComplication", 
        "possibleTreatment", 
        "primaryPrevention", 
        "riskFactor", 
        "secondaryPrevention", 
        "signOrSymptom", 
        "stage", 
        "subtype", 
        "typicalTest"
      ], 
      "subtypes": [
        "InfectiousDisease"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalCondition"
    }, 
    "MedicalConditionStage": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "A stage of a medical condition, such as 'Stage IIIa'.", 
      "comment_plain": "A stage of a medical condition, such as 'Stage IIIa'.", 
      "id": "MedicalConditionStage", 
      "label": "Medical Condition Stage", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "stageAsNumber", 
        "subStageSuffix"
      ], 
      "specific_properties": [
        "stageAsNumber", 
        "subStageSuffix"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/MedicalConditionStage"
    }, 
    "MedicalContraindication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but that these risks may be outweighed by other considerations or mitigated by other measures).", 
      "comment_plain": "A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications can be absolute (there are no reasonable circumstances for undertaking a course of action) or relative (the patient is at higher risk of complications, but that these risks may be outweighed by other considerations or mitigated by other measures).", 
      "id": "MedicalContraindication", 
      "label": "Medical Contraindication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalContraindication"
    }, 
    "MedicalDevice": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any object used in a medical capacity, such as to diagnose or treat a patient.", 
      "comment_plain": "Any object used in a medical capacity, such as to diagnose or treat a patient.", 
      "id": "MedicalDevice", 
      "label": "Medical Device", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "indication", 
        "postOp", 
        "preOp", 
        "procedure", 
        "purpose", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [
        "adverseOutcome", 
        "contraindication", 
        "indication", 
        "postOp", 
        "preOp", 
        "procedure", 
        "purpose", 
        "seriousAdverseOutcome"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalDevice"
    }, 
    "MedicalDevicePurpose": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Categories of medical devices, organized by the purpose or intended use of the device.", 
      "comment_plain": "Categories of medical devices, organized by the purpose or intended use of the device.", 
      "id": "MedicalDevicePurpose", 
      "instances": [
        "Diagnostic", 
        "Therapeutic"
      ], 
      "label": "Medical Device Purpose", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalDevicePurpose"
    }, 
    "MedicalEntity": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "The most generic type of entity related to health and the practice of medicine.", 
      "comment_plain": "The most generic type of entity related to health and the practice of medicine.", 
      "id": "MedicalEntity", 
      "label": "Medical Entity", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "subtypes": [
        "AnatomicalStructure", 
        "AnatomicalSystem", 
        "MedicalCause", 
        "MedicalCondition", 
        "MedicalContraindication", 
        "MedicalDevice", 
        "MedicalGuideline", 
        "MedicalIndication", 
        "MedicalIntangible", 
        "MedicalProcedure", 
        "MedicalRiskEstimator", 
        "MedicalRiskFactor", 
        "MedicalSignOrSymptom", 
        "MedicalStudy", 
        "MedicalTest", 
        "MedicalTherapy", 
        "SuperficialAnatomy"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/MedicalEntity"
    }, 
    "MedicalEnumeration": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible"
      ], 
      "comment": "Enumerations related to health and the practice of medicine.", 
      "comment_plain": "Enumerations related to health and the practice of medicine.", 
      "id": "MedicalEnumeration", 
      "label": "Medical Enumeration", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "DrugCostCategory", 
        "DrugPregnancyCategory", 
        "DrugPrescriptionStatus", 
        "InfectiousAgentClass", 
        "MedicalAudience", 
        "MedicalDevicePurpose", 
        "MedicalEvidenceLevel", 
        "MedicalImagingTechnique", 
        "MedicalObservationalStudyDesign", 
        "MedicalProcedureType", 
        "MedicalSpecialty", 
        "MedicalStudyStatus", 
        "MedicalTrialDesign", 
        "MedicineSystem", 
        "PhysicalActivityCategory", 
        "PhysicalExam"
      ], 
      "supertypes": [
        "MedicalIntangible"
      ], 
      "url": "http://schema.org/MedicalEnumeration"
    }, 
    "MedicalEvidenceLevel": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Level of evidence for a medical guideline. Enumerated type.", 
      "comment_plain": "Level of evidence for a medical guideline. Enumerated type.", 
      "id": "MedicalEvidenceLevel", 
      "instances": [
        "EvidenceLevelA", 
        "EvidenceLevelB", 
        "EvidenceLevelC"
      ], 
      "label": "Medical Evidence Level", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalEvidenceLevel"
    }, 
    "MedicalGuideline": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.", 
      "comment_plain": "Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.", 
      "id": "MedicalGuideline", 
      "label": "Medical Guideline", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "evidenceLevel", 
        "evidenceOrigin", 
        "guidelineDate", 
        "guidelineSubject"
      ], 
      "specific_properties": [
        "evidenceLevel", 
        "evidenceOrigin", 
        "guidelineDate", 
        "guidelineSubject"
      ], 
      "subtypes": [
        "MedicalGuidelineContraindication", 
        "MedicalGuidelineRecommendation"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalGuideline"
    }, 
    "MedicalGuidelineContraindication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalGuideline"
      ], 
      "comment": "A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.", 
      "comment_plain": "A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.", 
      "id": "MedicalGuidelineContraindication", 
      "label": "Medical Guideline Contraindication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "evidenceLevel", 
        "evidenceOrigin", 
        "guidelineDate", 
        "guidelineSubject"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalGuideline"
      ], 
      "url": "http://schema.org/MedicalGuidelineContraindication"
    }, 
    "MedicalGuidelineRecommendation": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalGuideline"
      ], 
      "comment": "A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.", 
      "comment_plain": "A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.", 
      "id": "MedicalGuidelineRecommendation", 
      "label": "Medical Guideline Recommendation", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "evidenceLevel", 
        "evidenceOrigin", 
        "guidelineDate", 
        "guidelineSubject", 
        "recommendationStrength"
      ], 
      "specific_properties": [
        "recommendationStrength"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalGuideline"
      ], 
      "url": "http://schema.org/MedicalGuidelineRecommendation"
    }, 
    "MedicalImagingTechnique": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Any medical imaging modality typically used for diagnostic purposes. Enumerated type.", 
      "comment_plain": "Any medical imaging modality typically used for diagnostic purposes. Enumerated type.", 
      "id": "MedicalImagingTechnique", 
      "instances": [
        "CT", 
        "MRI", 
        "PET", 
        "Ultrasound", 
        "XRay"
      ], 
      "label": "Medical Imaging Technique", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalImagingTechnique"
    }, 
    "MedicalIndication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.", 
      "comment_plain": "A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.", 
      "id": "MedicalIndication", 
      "label": "Medical Indication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "ApprovedIndication", 
        "PreventionIndication", 
        "TreatmentIndication"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalIndication"
    }, 
    "MedicalIntangible": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.", 
      "comment_plain": "A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.", 
      "id": "MedicalIntangible", 
      "label": "Medical Intangible", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "DDxElement", 
        "DoseSchedule", 
        "DrugCost", 
        "DrugLegalStatus", 
        "DrugStrength", 
        "MedicalCode", 
        "MedicalConditionStage", 
        "MedicalEnumeration"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalIntangible"
    }, 
    "MedicalObservationalStudy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalStudy"
      ], 
      "comment": "An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.", 
      "comment_plain": "An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.", 
      "id": "MedicalObservationalStudy", 
      "label": "Medical Observational Study", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "outcome", 
        "population", 
        "sponsor", 
        "status", 
        "studyLocation", 
        "studySubject", 
        "studyDesign"
      ], 
      "specific_properties": [
        "studyDesign"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalStudy"
      ], 
      "url": "http://schema.org/MedicalObservationalStudy"
    }, 
    "MedicalObservationalStudyDesign": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Design models for observational medical studies. Enumerated type.", 
      "comment_plain": "Design models for observational medical studies. Enumerated type.", 
      "id": "MedicalObservationalStudyDesign", 
      "instances": [
        "CaseSeries", 
        "CohortStudy", 
        "CrossSectional", 
        "Longitudinal", 
        "Observational", 
        "Registry"
      ], 
      "label": "Medical Observational Study Design", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalObservationalStudyDesign"
    }, 
    "MedicalOrganization": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A medical organization, such as a doctor's office or clinic.", 
      "comment_plain": "A medical organization, such as a doctor's office or clinic.", 
      "id": "MedicalOrganization", 
      "label": "Medical Organization", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Dentist", 
        "DiagnosticLab", 
        "Hospital", 
        "MedicalClinic", 
        "Optician", 
        "Pharmacy", 
        "Physician", 
        "VeterinaryCare"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/MedicalOrganization"
    }, 
    "MedicalProcedure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A process of care used in either a diagnostic, therapeutic, or palliative capacity that relies on invasive (surgical), non-invasive, or percutaneous techniques.", 
      "comment_plain": "A process of care used in either a diagnostic, therapeutic, or palliative capacity that relies on invasive (surgical), non-invasive, or percutaneous techniques.", 
      "id": "MedicalProcedure", 
      "label": "Medical Procedure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "followup", 
        "howPerformed", 
        "preparation", 
        "procedureType"
      ], 
      "specific_properties": [
        "followup", 
        "howPerformed", 
        "preparation", 
        "procedureType"
      ], 
      "subtypes": [
        "DiagnosticProcedure", 
        "PalliativeProcedure", 
        "TherapeuticProcedure"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalProcedure"
    }, 
    "MedicalProcedureType": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "An enumeration that describes different types of medical procedures.", 
      "comment_plain": "An enumeration that describes different types of medical procedures.", 
      "id": "MedicalProcedureType", 
      "instances": [
        "NoninvasiveProcedure", 
        "PercutaneousProcedure", 
        "SurgicalProcedure"
      ], 
      "label": "Medical Procedure Type", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalProcedureType"
    }, 
    "MedicalRiskCalculator": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalRiskEstimator"
      ], 
      "comment": "A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.", 
      "comment_plain": "A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.", 
      "id": "MedicalRiskCalculator", 
      "label": "Medical Risk Calculator", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "estimatesRiskOf", 
        "includedRiskFactor"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalRiskEstimator"
      ], 
      "url": "http://schema.org/MedicalRiskCalculator"
    }, 
    "MedicalRiskEstimator": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any rule set or interactive tool for estimating the risk of developing a complication or condition.", 
      "comment_plain": "Any rule set or interactive tool for estimating the risk of developing a complication or condition.", 
      "id": "MedicalRiskEstimator", 
      "label": "Medical Risk Estimator", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "estimatesRiskOf", 
        "includedRiskFactor"
      ], 
      "specific_properties": [
        "estimatesRiskOf", 
        "includedRiskFactor"
      ], 
      "subtypes": [
        "MedicalRiskCalculator", 
        "MedicalRiskScore"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalRiskEstimator"
    }, 
    "MedicalRiskFactor": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.", 
      "comment_plain": "A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.", 
      "id": "MedicalRiskFactor", 
      "label": "Medical Risk Factor", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "increasesRiskOf"
      ], 
      "specific_properties": [
        "increasesRiskOf"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalRiskFactor"
    }, 
    "MedicalRiskScore": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalRiskEstimator"
      ], 
      "comment": "A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.", 
      "comment_plain": "A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.", 
      "id": "MedicalRiskScore", 
      "label": "Medical Risk Score", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "estimatesRiskOf", 
        "includedRiskFactor", 
        "algorithm"
      ], 
      "specific_properties": [
        "algorithm"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalRiskEstimator"
      ], 
      "url": "http://schema.org/MedicalRiskScore"
    }, 
    "MedicalScholarlyArticle": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article", 
        "ScholarlyArticle"
      ], 
      "comment": "A scholarly article in the medical domain.", 
      "comment_plain": "A scholarly article in the medical domain.", 
      "id": "MedicalScholarlyArticle", 
      "label": "Medical Scholarly Article", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount", 
        "citation", 
        "publicationType"
      ], 
      "specific_properties": [
        "citation", 
        "publicationType"
      ], 
      "subtypes": [], 
      "supertypes": [
        "ScholarlyArticle"
      ], 
      "url": "http://schema.org/MedicalScholarlyArticle"
    }, 
    "MedicalSign": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalSignOrSymptom"
      ], 
      "comment": "Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.", 
      "comment_plain": "Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.", 
      "id": "MedicalSign", 
      "label": "Medical Sign", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "cause", 
        "possibleTreatment", 
        "identifyingExam", 
        "identifyingTest"
      ], 
      "specific_properties": [
        "identifyingExam", 
        "identifyingTest"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalSignOrSymptom"
      ], 
      "url": "http://schema.org/MedicalSign"
    }, 
    "MedicalSignOrSymptom": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any indication of the existence of a medical condition or disease.", 
      "comment_plain": "Any indication of the existence of a medical condition or disease.", 
      "id": "MedicalSignOrSymptom", 
      "label": "Medical Sign or Symptom", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "cause", 
        "possibleTreatment"
      ], 
      "specific_properties": [
        "cause", 
        "possibleTreatment"
      ], 
      "subtypes": [
        "MedicalSign", 
        "MedicalSymptom"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalSignOrSymptom"
    }, 
    "MedicalSpecialty": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.", 
      "comment_plain": "Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.", 
      "id": "MedicalSpecialty", 
      "instances": [
        "Anesthesia", 
        "Cardiovascular", 
        "CommunityHealth", 
        "Dentistry", 
        "Dermatologic", 
        "DietNutrition", 
        "Emergency", 
        "Endocrine", 
        "Gastroenterologic", 
        "Genetic", 
        "Geriatric", 
        "Gynecologic", 
        "Hematologic", 
        "Infectious", 
        "LaboratoryScience", 
        "Midwifery", 
        "Musculoskeletal", 
        "Neurologic", 
        "Nursing", 
        "Obstetric", 
        "OccupationalTherapy", 
        "Oncologic", 
        "Optometic", 
        "Otolaryngologic", 
        "Pathology", 
        "Pediatric", 
        "PharmacySpecialty", 
        "Physiotherapy", 
        "PlasticSurgery", 
        "Podiatric", 
        "PrimaryCare", 
        "Psychiatric", 
        "PublicHealth", 
        "Pulmonary", 
        "Radiograpy", 
        "Renal", 
        "RespiratoryTherapy", 
        "Rheumatologic", 
        "SpeechPathology", 
        "Surgical", 
        "Toxicologic", 
        "Urologic"
      ], 
      "label": "Medical Specialty", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Specialty", 
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalSpecialty"
    }, 
    "MedicalStudy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.", 
      "comment_plain": "A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.", 
      "id": "MedicalStudy", 
      "label": "Medical Study", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "outcome", 
        "population", 
        "sponsor", 
        "status", 
        "studyLocation", 
        "studySubject"
      ], 
      "specific_properties": [
        "outcome", 
        "population", 
        "sponsor", 
        "status", 
        "studyLocation", 
        "studySubject"
      ], 
      "subtypes": [
        "MedicalObservationalStudy", 
        "MedicalTrial"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalStudy"
    }, 
    "MedicalStudyStatus": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "The status of a medical study. Enumerated type.", 
      "comment_plain": "The status of a medical study. Enumerated type.", 
      "id": "MedicalStudyStatus", 
      "instances": [
        "ActiveNotRecruiting", 
        "Completed", 
        "EnrollingByInvitation", 
        "NotYetRecruiting", 
        "Recruiting", 
        "ResultsAvailable", 
        "ResultsNotAvailable", 
        "Suspended", 
        "Terminated", 
        "Withdrawn"
      ], 
      "label": "Medical Study Status", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalStudyStatus"
    }, 
    "MedicalSymptom": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalSignOrSymptom"
      ], 
      "comment": "Any indication of the existence of a medical condition or disease that is apparent to the patient.", 
      "comment_plain": "Any indication of the existence of a medical condition or disease that is apparent to the patient.", 
      "id": "MedicalSymptom", 
      "label": "Medical Symptom", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "cause", 
        "possibleTreatment"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalSignOrSymptom"
      ], 
      "url": "http://schema.org/MedicalSymptom"
    }, 
    "MedicalTest": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any medical test, typically performed for diagnostic purposes.", 
      "comment_plain": "Any medical test, typically performed for diagnostic purposes.", 
      "id": "MedicalTest", 
      "label": "Medical Test", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice"
      ], 
      "specific_properties": [
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice"
      ], 
      "subtypes": [
        "BloodTest", 
        "DiagnosticProcedure", 
        "ImagingTest", 
        "MedicalTestPanel", 
        "PathologyTest"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalTest"
    }, 
    "MedicalTestPanel": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTest"
      ], 
      "comment": "Any collection of tests commonly ordered together.", 
      "comment_plain": "Any collection of tests commonly ordered together.", 
      "id": "MedicalTestPanel", 
      "label": "Medical Test Panel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice", 
        "subTest"
      ], 
      "specific_properties": [
        "subTest"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTest"
      ], 
      "url": "http://schema.org/MedicalTestPanel"
    }, 
    "MedicalTherapy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.", 
      "comment_plain": "Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.", 
      "id": "MedicalTherapy", 
      "label": "Medical Therapy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "subtypes": [
        "DietarySupplement", 
        "Drug", 
        "DrugClass", 
        "LifestyleModification", 
        "PalliativeProcedure", 
        "PhysicalTherapy", 
        "PsychologicalTreatment", 
        "RadiationTherapy", 
        "TherapeuticProcedure"
      ], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/MedicalTherapy"
    }, 
    "MedicalTrial": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalStudy"
      ], 
      "comment": "A medical trial is a type of medical study that uses scientific process used to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.", 
      "comment_plain": "A medical trial is a type of medical study that uses scientific process used to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.", 
      "id": "MedicalTrial", 
      "label": "Medical Trial", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "outcome", 
        "population", 
        "sponsor", 
        "status", 
        "studyLocation", 
        "studySubject", 
        "phase", 
        "trialDesign"
      ], 
      "specific_properties": [
        "phase", 
        "trialDesign"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalStudy"
      ], 
      "url": "http://schema.org/MedicalTrial"
    }, 
    "MedicalTrialDesign": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Design models for medical trials. Enumerated type.", 
      "comment_plain": "Design models for medical trials. Enumerated type.", 
      "id": "MedicalTrialDesign", 
      "instances": [
        "DoubleBlindedTrial", 
        "InternationalTrial", 
        "MultiCenterTrial", 
        "OpenTrial", 
        "PlaceboControlledTrial", 
        "RandomizedTrial", 
        "SingleBlindedTrial", 
        "SingleCenterTrial", 
        "TripleBlindedTrial"
      ], 
      "label": "Medical Trial Design", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicalTrialDesign"
    }, 
    "MedicalWebPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "A web page that provides medical information.", 
      "comment_plain": "A web page that provides medical information.", 
      "id": "MedicalWebPage", 
      "label": "Medical Web Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty", 
        "aspect"
      ], 
      "specific_properties": [
        "aspect"
      ], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/MedicalWebPage"
    }, 
    "MedicineSystem": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Systems of medical practice.", 
      "comment_plain": "Systems of medical practice.", 
      "id": "MedicineSystem", 
      "instances": [
        "Ayurvedic", 
        "Chiropractic", 
        "Homeopathic", 
        "Osteopathic", 
        "TraditionalChinese", 
        "WesternConventional"
      ], 
      "label": "Medicine System", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/MedicineSystem"
    }, 
    "MensClothingStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A men's clothing store.", 
      "comment_plain": "A men's clothing store.", 
      "id": "MensClothingStore", 
      "label": "Mens Clothing Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/MensClothingStore"
    }, 
    "MiddleSchool": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "A middle school.", 
      "comment_plain": "A middle school.", 
      "id": "MiddleSchool", 
      "label": "Middle School", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/MiddleSchool"
    }, 
    "MobileApplication": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "SoftwareApplication"
      ], 
      "comment": "A mobile software application.", 
      "comment_plain": "A mobile software application.", 
      "id": "MobileApplication", 
      "label": "Mobile Application", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "applicationCategory", 
        "applicationSubCategory", 
        "applicationSuite", 
        "countriesNotSupported", 
        "countriesSupported", 
        "device", 
        "downloadUrl", 
        "featureList", 
        "fileFormat", 
        "fileSize", 
        "installUrl", 
        "memoryRequirements", 
        "operatingSystem", 
        "permissions", 
        "processorRequirements", 
        "releaseNotes", 
        "requirements", 
        "screenshot", 
        "softwareVersion", 
        "storageRequirements", 
        "carrierRequirements"
      ], 
      "specific_properties": [
        "carrierRequirements"
      ], 
      "subtypes": [], 
      "supertypes": [
        "SoftwareApplication"
      ], 
      "url": "http://schema.org/MobileApplication"
    }, 
    "MobilePhoneStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A mobile-phone store.", 
      "comment_plain": "A mobile-phone store.", 
      "id": "MobilePhoneStore", 
      "label": "Mobile Phone Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/MobilePhoneStore"
    }, 
    "Mosque": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A mosque.", 
      "comment_plain": "A mosque.", 
      "id": "Mosque", 
      "label": "Mosque", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/Mosque"
    }, 
    "Motel": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "LodgingBusiness"
      ], 
      "comment": "A motel.", 
      "comment_plain": "A motel.", 
      "id": "Motel", 
      "label": "Motel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LodgingBusiness"
      ], 
      "url": "http://schema.org/Motel"
    }, 
    "MotorcycleDealer": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "A motorcycle dealer.", 
      "comment_plain": "A motorcycle dealer.", 
      "id": "MotorcycleDealer", 
      "label": "Motorcycle Dealer", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/MotorcycleDealer"
    }, 
    "MotorcycleRepair": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "AutomotiveBusiness"
      ], 
      "comment": "A motorcycle repair shop.", 
      "comment_plain": "A motorcycle repair shop.", 
      "id": "MotorcycleRepair", 
      "label": "Motorcycle Repair", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AutomotiveBusiness"
      ], 
      "url": "http://schema.org/MotorcycleRepair"
    }, 
    "Mountain": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform"
      ], 
      "comment": "A mountain, like Mount Whitney or Mount Everest", 
      "comment_plain": "A mountain, like Mount Whitney or Mount Everest", 
      "id": "Mountain", 
      "label": "Mountain", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Landform"
      ], 
      "url": "http://schema.org/Mountain"
    }, 
    "Movie": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A movie.", 
      "comment_plain": "A movie.", 
      "id": "Movie", 
      "label": "Movie", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "actor", 
        "actors", 
        "director", 
        "duration", 
        "musicBy", 
        "producer", 
        "productionCompany", 
        "trailer"
      ], 
      "specific_properties": [
        "actor", 
        "actors", 
        "director", 
        "duration", 
        "musicBy", 
        "producer", 
        "productionCompany", 
        "trailer"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Movie"
    }, 
    "MovieRentalStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A movie rental store.", 
      "comment_plain": "A movie rental store.", 
      "id": "MovieRentalStore", 
      "label": "Movie Rental Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/MovieRentalStore"
    }, 
    "MovieTheater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A movie theater.", 
      "comment_plain": "A movie theater.", 
      "id": "MovieTheater", 
      "label": "Movie Theater", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness", 
        "CivicStructure"
      ], 
      "url": "http://schema.org/MovieTheater"
    }, 
    "MovingCompany": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A moving company.", 
      "comment_plain": "A moving company.", 
      "id": "MovingCompany", 
      "label": "Moving Company", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/MovingCompany"
    }, 
    "Muscle": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.", 
      "comment_plain": "A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.", 
      "id": "Muscle", 
      "label": "Muscle", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "action", 
        "antagonist", 
        "bloodSupply", 
        "insertion", 
        "nerve", 
        "origin"
      ], 
      "specific_properties": [
        "action", 
        "antagonist", 
        "bloodSupply", 
        "insertion", 
        "nerve", 
        "origin"
      ], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Muscle"
    }, 
    "Museum": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A museum.", 
      "comment_plain": "A museum.", 
      "id": "Museum", 
      "label": "Museum", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Museum"
    }, 
    "MusicAlbum": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MusicPlaylist"
      ], 
      "comment": "A collection of music tracks.", 
      "comment_plain": "A collection of music tracks.", 
      "id": "MusicAlbum", 
      "label": "Music Album", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "numTracks", 
        "track", 
        "tracks", 
        "byArtist"
      ], 
      "specific_properties": [
        "byArtist"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MusicPlaylist"
      ], 
      "url": "http://schema.org/MusicAlbum"
    }, 
    "MusicEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Music event.", 
      "comment_plain": "Event type: Music event.", 
      "id": "MusicEvent", 
      "label": "Music Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/MusicEvent"
    }, 
    "MusicGroup": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "PerformingGroup"
      ], 
      "comment": "A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.", 
      "comment_plain": "A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.", 
      "id": "MusicGroup", 
      "label": "Music Group", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "album", 
        "albums", 
        "musicGroupMember", 
        "track", 
        "tracks"
      ], 
      "specific_properties": [
        "album", 
        "albums", 
        "musicGroupMember", 
        "track", 
        "tracks"
      ], 
      "subtypes": [], 
      "supertypes": [
        "PerformingGroup"
      ], 
      "url": "http://schema.org/MusicGroup"
    }, 
    "MusicPlaylist": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A collection of music tracks in playlist form.", 
      "comment_plain": "A collection of music tracks in playlist form.", 
      "id": "MusicPlaylist", 
      "label": "Music Playlist", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "numTracks", 
        "track", 
        "tracks"
      ], 
      "specific_properties": [
        "numTracks", 
        "track", 
        "tracks"
      ], 
      "subtypes": [
        "MusicAlbum"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/MusicPlaylist"
    }, 
    "MusicRecording": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A music recording (track), usually a single song.", 
      "comment_plain": "A music recording (track), usually a single song.", 
      "id": "MusicRecording", 
      "label": "Music Recording", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "byArtist", 
        "duration", 
        "inAlbum", 
        "inPlaylist"
      ], 
      "specific_properties": [
        "byArtist", 
        "duration", 
        "inAlbum", 
        "inPlaylist"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/MusicRecording"
    }, 
    "MusicStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A music store.", 
      "comment_plain": "A music store.", 
      "id": "MusicStore", 
      "label": "Music Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/MusicStore"
    }, 
    "MusicVenue": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A music venue.", 
      "comment_plain": "A music venue.", 
      "id": "MusicVenue", 
      "label": "Music Venue", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/MusicVenue"
    }, 
    "MusicVideoObject": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MediaObject"
      ], 
      "comment": "A music video file.", 
      "comment_plain": "A music video file.", 
      "id": "MusicVideoObject", 
      "label": "Music Video Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MediaObject"
      ], 
      "url": "http://schema.org/MusicVideoObject"
    }, 
    "NGO": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "Organization: Non-governmental Organization.", 
      "comment_plain": "Organization: Non-governmental Organization.", 
      "id": "NGO", 
      "label": "NGO", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/NGO"
    }, 
    "NailSalon": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "A nail salon.", 
      "comment_plain": "A nail salon.", 
      "id": "NailSalon", 
      "label": "Nail Salon", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness"
      ], 
      "url": "http://schema.org/NailSalon"
    }, 
    "Nerve": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.", 
      "comment_plain": "A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.", 
      "id": "Nerve", 
      "label": "Nerve", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "branch", 
        "nerveMotor", 
        "sensoryUnit", 
        "sourcedFrom"
      ], 
      "specific_properties": [
        "branch", 
        "nerveMotor", 
        "sensoryUnit", 
        "sourcedFrom"
      ], 
      "subtypes": [], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Nerve"
    }, 
    "NewsArticle": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article"
      ], 
      "comment": "A news article", 
      "comment_plain": "A news article", 
      "id": "NewsArticle", 
      "label": "News Article", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount", 
        "dateline", 
        "printColumn", 
        "printEdition", 
        "printPage", 
        "printSection"
      ], 
      "specific_properties": [
        "dateline", 
        "printColumn", 
        "printEdition", 
        "printPage", 
        "printSection"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Article"
      ], 
      "url": "http://schema.org/NewsArticle"
    }, 
    "NightClub": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "EntertainmentBusiness"
      ], 
      "comment": "A nightclub or discotheque.", 
      "comment_plain": "A nightclub or discotheque.", 
      "id": "NightClub", 
      "label": "Night Club", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EntertainmentBusiness"
      ], 
      "url": "http://schema.org/NightClub"
    }, 
    "Notary": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "ProfessionalService"
      ], 
      "comment": "A notary.", 
      "comment_plain": "A notary.", 
      "id": "Notary", 
      "label": "Notary", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService"
      ], 
      "url": "http://schema.org/Notary"
    }, 
    "NutritionInformation": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "Nutritional information about the recipe.", 
      "comment_plain": "Nutritional information about the recipe.", 
      "id": "NutritionInformation", 
      "label": "Nutrition Information", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "calories", 
        "carbohydrateContent", 
        "cholesterolContent", 
        "fatContent", 
        "fiberContent", 
        "proteinContent", 
        "saturatedFatContent", 
        "servingSize", 
        "sodiumContent", 
        "sugarContent", 
        "transFatContent", 
        "unsaturatedFatContent"
      ], 
      "specific_properties": [
        "calories", 
        "carbohydrateContent", 
        "cholesterolContent", 
        "fatContent", 
        "fiberContent", 
        "proteinContent", 
        "saturatedFatContent", 
        "servingSize", 
        "sodiumContent", 
        "sugarContent", 
        "transFatContent", 
        "unsaturatedFatContent"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/NutritionInformation"
    }, 
    "OceanBodyOfWater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "An ocean (for example, the Pacific).", 
      "comment_plain": "An ocean (for example, the Pacific).", 
      "id": "OceanBodyOfWater", 
      "label": "Ocean Body of Water", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/OceanBodyOfWater"
    }, 
    "Offer": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "An offer to sell an item\u2014for example, an offer to sell a product, the DVD of a movie, or tickets to an event.", 
      "comment_plain": "An offer to sell an item\u2014for example, an offer to sell a product, the DVD of a movie, or tickets to an event.", 
      "id": "Offer", 
      "label": "Offer", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "acceptedPaymentMethod", 
        "addOn", 
        "advanceBookingRequirement", 
        "aggregateRating", 
        "availability", 
        "availabilityEnds", 
        "availabilityStarts", 
        "availableAtOrFrom", 
        "availableDeliveryMethod", 
        "businessFunction", 
        "category", 
        "deliveryLeadTime", 
        "eligibleCustomerType", 
        "eligibleDuration", 
        "eligibleQuantity", 
        "eligibleRegion", 
        "eligibleTransactionVolume", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "includesObject", 
        "inventoryLevel", 
        "itemCondition", 
        "itemOffered", 
        "mpn", 
        "price", 
        "priceCurrency", 
        "priceSpecification", 
        "priceValidUntil", 
        "review", 
        "reviews", 
        "seller", 
        "serialNumber", 
        "sku", 
        "validFrom", 
        "validThrough", 
        "warranty"
      ], 
      "specific_properties": [
        "acceptedPaymentMethod", 
        "addOn", 
        "advanceBookingRequirement", 
        "aggregateRating", 
        "availability", 
        "availabilityEnds", 
        "availabilityStarts", 
        "availableAtOrFrom", 
        "availableDeliveryMethod", 
        "businessFunction", 
        "category", 
        "deliveryLeadTime", 
        "eligibleCustomerType", 
        "eligibleDuration", 
        "eligibleQuantity", 
        "eligibleRegion", 
        "eligibleTransactionVolume", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "includesObject", 
        "inventoryLevel", 
        "itemCondition", 
        "itemOffered", 
        "mpn", 
        "price", 
        "priceCurrency", 
        "priceSpecification", 
        "priceValidUntil", 
        "review", 
        "reviews", 
        "seller", 
        "serialNumber", 
        "sku", 
        "validFrom", 
        "validThrough", 
        "warranty"
      ], 
      "subtypes": [
        "AggregateOffer"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Offer"
    }, 
    "OfferItemCondition": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A list of possible conditions for the item for sale.", 
      "comment_plain": "A list of possible conditions for the item for sale.", 
      "id": "OfferItemCondition", 
      "instances": [
        "DamagedCondition", 
        "NewCondition", 
        "RefurbishedCondition", 
        "UsedCondition"
      ], 
      "label": "Offer Item Condition", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/OfferItemCondition"
    }, 
    "OfficeEquipmentStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "An office equipment store.", 
      "comment_plain": "An office equipment store.", 
      "id": "OfficeEquipmentStore", 
      "label": "Office Equipment Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/OfficeEquipmentStore"
    }, 
    "OpeningHoursSpecification": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A structured value providing information about the opening hours of a place or a certain service inside a place.", 
      "comment_plain": "A structured value providing information about the opening hours of a place or a certain service inside a place.", 
      "id": "OpeningHoursSpecification", 
      "label": "Opening Hours Specification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "closes", 
        "dayOfWeek", 
        "opens", 
        "validFrom", 
        "validThrough"
      ], 
      "specific_properties": [
        "closes", 
        "dayOfWeek", 
        "opens", 
        "validFrom", 
        "validThrough"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/OpeningHoursSpecification"
    }, 
    "Optician": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "An optician's store.", 
      "comment_plain": "An optician's store.", 
      "id": "Optician", 
      "label": "Optician", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/Optician"
    }, 
    "Organization": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "An organization such as a school, NGO, corporation, club, etc.", 
      "comment_plain": "An organization such as a school, NGO, corporation, club, etc.", 
      "id": "Organization", 
      "label": "Organization", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "subtypes": [
        "Corporation", 
        "EducationalOrganization", 
        "GovernmentOrganization", 
        "LocalBusiness", 
        "NGO", 
        "PerformingGroup", 
        "SportsTeam"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Organization"
    }, 
    "OutletStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "An outlet store.", 
      "comment_plain": "An outlet store.", 
      "id": "OutletStore", 
      "label": "Outlet Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/OutletStore"
    }, 
    "OwnershipInfo": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A structured value providing information about when a certain organization or person owned a certain product.", 
      "comment_plain": "A structured value providing information about when a certain organization or person owned a certain product.", 
      "id": "OwnershipInfo", 
      "label": "Ownership Info", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "acquiredFrom", 
        "ownedFrom", 
        "ownedThrough", 
        "typeOfGood"
      ], 
      "specific_properties": [
        "acquiredFrom", 
        "ownedFrom", 
        "ownedThrough", 
        "typeOfGood"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/OwnershipInfo"
    }, 
    "Painting": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A painting.", 
      "comment_plain": "A painting.", 
      "id": "Painting", 
      "label": "Painting", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Painting"
    }, 
    "PalliativeProcedure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalProcedure"
      ], 
      "comment": "A medical procedure intended primarly for palliative purposes, aimed at relieving the symptoms of an underlying health condition.", 
      "comment_plain": "A medical procedure intended primarly for palliative purposes, aimed at relieving the symptoms of an underlying health condition.", 
      "id": "PalliativeProcedure", 
      "label": "Palliative Procedure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "followup", 
        "howPerformed", 
        "preparation", 
        "procedureType"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalProcedure", 
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/PalliativeProcedure"
    }, 
    "ParcelService": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration", 
        "DeliveryMethod"
      ], 
      "comment": "A private parcel service as the delivery mode available for a certain offer.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#DHL\nhttp://purl.org/goodrelations/v1#FederalExpress\nhttp://purl.org/goodrelations/v1#UPS", 
      "comment_plain": "A private parcel service as the delivery mode available for a certain offer.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#DHL\nhttp://purl.org/goodrelations/v1#FederalExpress\nhttp://purl.org/goodrelations/v1#UPS", 
      "id": "ParcelService", 
      "label": "Parcel Service", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DeliveryMethod"
      ], 
      "url": "http://schema.org/ParcelService"
    }, 
    "ParentAudience": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Audience", 
        "PeopleAudience"
      ], 
      "comment": "A set of characteristics describing parents, who can be interested in viewing some content", 
      "comment_plain": "A set of characteristics describing parents, who can be interested in viewing some content", 
      "id": "ParentAudience", 
      "label": "Parent Audience", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "healthCondition", 
        "suggestedGender", 
        "suggestedMaxAge", 
        "suggestedMinAge", 
        "childMaxAge", 
        "childMinAge"
      ], 
      "specific_properties": [
        "childMaxAge", 
        "childMinAge"
      ], 
      "subtypes": [], 
      "supertypes": [
        "PeopleAudience"
      ], 
      "url": "http://schema.org/ParentAudience"
    }, 
    "Park": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A park.", 
      "comment_plain": "A park.", 
      "id": "Park", 
      "label": "Park", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Park"
    }, 
    "ParkingFacility": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A parking lot or other parking facility.", 
      "comment_plain": "A parking lot or other parking facility.", 
      "id": "ParkingFacility", 
      "label": "Parking Facility", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/ParkingFacility"
    }, 
    "PathologyTest": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTest"
      ], 
      "comment": "A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.", 
      "comment_plain": "A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.", 
      "id": "PathologyTest", 
      "label": "Pathology Test", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "affectedBy", 
        "normalRange", 
        "signDetected", 
        "usedToDiagnose", 
        "usesDevice", 
        "tissueSample"
      ], 
      "specific_properties": [
        "tissueSample"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTest"
      ], 
      "url": "http://schema.org/PathologyTest"
    }, 
    "PawnShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A pawnstore.", 
      "comment_plain": "A pawnstore.", 
      "id": "PawnShop", 
      "label": "Pawn Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/PawnShop"
    }, 
    "PaymentChargeSpecification": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue", 
        "PriceSpecification"
      ], 
      "comment": "The costs of settling the payment using a particular payment method.", 
      "comment_plain": "The costs of settling the payment using a particular payment method.", 
      "id": "PaymentChargeSpecification", 
      "label": "Payment Charge Specification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "eligibleQuantity", 
        "eligibleTransactionVolume", 
        "maxPrice", 
        "minPrice", 
        "price", 
        "priceCurrency", 
        "validFrom", 
        "validThrough", 
        "valueAddedTaxIncluded", 
        "appliesToDeliveryMethod", 
        "appliesToPaymentMethod"
      ], 
      "specific_properties": [
        "appliesToDeliveryMethod", 
        "appliesToPaymentMethod"
      ], 
      "subtypes": [], 
      "supertypes": [
        "PriceSpecification"
      ], 
      "url": "http://schema.org/PaymentChargeSpecification"
    }, 
    "PaymentMethod": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#ByBankTransferInAdvance\nhttp://purl.org/goodrelations/v1#ByInvoice\nhttp://purl.org/goodrelations/v1#Cash\nhttp://purl.org/goodrelations/v1#CheckInAdvance\nhttp://purl.org/goodrelations/v1#COD\nhttp://purl.org/goodrelations/v1#DirectDebit\nhttp://purl.org/goodrelations/v1#GoogleCheckout\nhttp://purl.org/goodrelations/v1#PayPal\nhttp://purl.org/goodrelations/v1#PaySwarm", 
      "comment_plain": "A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#ByBankTransferInAdvance\nhttp://purl.org/goodrelations/v1#ByInvoice\nhttp://purl.org/goodrelations/v1#Cash\nhttp://purl.org/goodrelations/v1#CheckInAdvance\nhttp://purl.org/goodrelations/v1#COD\nhttp://purl.org/goodrelations/v1#DirectDebit\nhttp://purl.org/goodrelations/v1#GoogleCheckout\nhttp://purl.org/goodrelations/v1#PayPal\nhttp://purl.org/goodrelations/v1#PaySwarm", 
      "id": "PaymentMethod", 
      "label": "Payment Method", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "CreditCard"
      ], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/PaymentMethod"
    }, 
    "PeopleAudience": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Audience"
      ], 
      "comment": "A set of characteristics belonging to people, e.g. who compose an item's target audience.", 
      "comment_plain": "A set of characteristics belonging to people, e.g. who compose an item's target audience.", 
      "id": "PeopleAudience", 
      "label": "People Audience", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "healthCondition", 
        "suggestedGender", 
        "suggestedMaxAge", 
        "suggestedMinAge"
      ], 
      "specific_properties": [
        "healthCondition", 
        "suggestedGender", 
        "suggestedMaxAge", 
        "suggestedMinAge"
      ], 
      "subtypes": [
        "MedicalAudience", 
        "ParentAudience"
      ], 
      "supertypes": [
        "Audience"
      ], 
      "url": "http://schema.org/PeopleAudience"
    }, 
    "PerformingArtsTheater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A theatre or other performing art center.", 
      "comment_plain": "A theatre or other performing art center.", 
      "id": "PerformingArtsTheater", 
      "label": "Performing Arts Theater", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/PerformingArtsTheater"
    }, 
    "PerformingGroup": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "A performance group, such as a band, an orchestra, or a circus.", 
      "comment_plain": "A performance group, such as a band, an orchestra, or a circus.", 
      "id": "PerformingGroup", 
      "label": "Performing Group", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "DanceGroup", 
        "MusicGroup", 
        "TheaterGroup"
      ], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/PerformingGroup"
    }, 
    "Person": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "A person (alive, dead, undead, or fictional).", 
      "comment_plain": "A person (alive, dead, undead, or fictional).", 
      "id": "Person", 
      "label": "Person", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "additionalName", 
        "address", 
        "affiliation", 
        "alumniOf", 
        "award", 
        "awards", 
        "birthDate", 
        "brand", 
        "children", 
        "colleague", 
        "colleagues", 
        "contactPoint", 
        "contactPoints", 
        "deathDate", 
        "duns", 
        "email", 
        "familyName", 
        "faxNumber", 
        "follows", 
        "gender", 
        "givenName", 
        "globalLocationNumber", 
        "hasPOS", 
        "homeLocation", 
        "honorificPrefix", 
        "honorificSuffix", 
        "interactionCount", 
        "isicV4", 
        "jobTitle", 
        "knows", 
        "makesOffer", 
        "memberOf", 
        "naics", 
        "nationality", 
        "owns", 
        "parent", 
        "parents", 
        "performerIn", 
        "relatedTo", 
        "seeks", 
        "sibling", 
        "siblings", 
        "spouse", 
        "taxID", 
        "telephone", 
        "vatID", 
        "workLocation", 
        "worksFor"
      ], 
      "specific_properties": [
        "additionalName", 
        "address", 
        "affiliation", 
        "alumniOf", 
        "award", 
        "awards", 
        "birthDate", 
        "brand", 
        "children", 
        "colleague", 
        "colleagues", 
        "contactPoint", 
        "contactPoints", 
        "deathDate", 
        "duns", 
        "email", 
        "familyName", 
        "faxNumber", 
        "follows", 
        "gender", 
        "givenName", 
        "globalLocationNumber", 
        "hasPOS", 
        "homeLocation", 
        "honorificPrefix", 
        "honorificSuffix", 
        "interactionCount", 
        "isicV4", 
        "jobTitle", 
        "knows", 
        "makesOffer", 
        "memberOf", 
        "naics", 
        "nationality", 
        "owns", 
        "parent", 
        "parents", 
        "performerIn", 
        "relatedTo", 
        "seeks", 
        "sibling", 
        "siblings", 
        "spouse", 
        "taxID", 
        "telephone", 
        "vatID", 
        "workLocation", 
        "worksFor"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Person"
    }, 
    "PetStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A pet store.", 
      "comment_plain": "A pet store.", 
      "id": "PetStore", 
      "label": "Pet Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/PetStore"
    }, 
    "Pharmacy": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A pharmacy or drugstore.", 
      "comment_plain": "A pharmacy or drugstore.", 
      "id": "Pharmacy", 
      "label": "Pharmacy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/Pharmacy"
    }, 
    "Photograph": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A photograph.", 
      "comment_plain": "A photograph.", 
      "id": "Photograph", 
      "label": "Photograph", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Photograph"
    }, 
    "PhysicalActivity": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy", 
        "LifestyleModification"
      ], 
      "comment": "Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.", 
      "comment_plain": "Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.", 
      "id": "PhysicalActivity", 
      "label": "Physical Activity", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "associatedAnatomy", 
        "category", 
        "epidemiology", 
        "pathophysiology"
      ], 
      "specific_properties": [
        "associatedAnatomy", 
        "category", 
        "epidemiology", 
        "pathophysiology"
      ], 
      "subtypes": [
        "ExercisePlan"
      ], 
      "supertypes": [
        "LifestyleModification"
      ], 
      "url": "http://schema.org/PhysicalActivity"
    }, 
    "PhysicalActivityCategory": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "Categories of physical activity, organized by physiologic classification.", 
      "comment_plain": "Categories of physical activity, organized by physiologic classification.", 
      "id": "PhysicalActivityCategory", 
      "instances": [
        "AerobicActivity", 
        "AnaerobicActivity", 
        "Balance", 
        "Flexibility", 
        "LeisureTimeActivity", 
        "OccupationalActivity", 
        "StrengthTraining"
      ], 
      "label": "Physical Activity Category", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/PhysicalActivityCategory"
    }, 
    "PhysicalExam": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "MedicalEnumeration"
      ], 
      "comment": "A type of physical examination of a patient performed by a physician. Enumerated type.", 
      "comment_plain": "A type of physical examination of a patient performed by a physician. Enumerated type.", 
      "id": "PhysicalExam", 
      "instances": [
        "Abdomen", 
        "Appearance", 
        "CardiovascularExam", 
        "Ear", 
        "Eye", 
        "Genitourinary", 
        "Head", 
        "Lung", 
        "MusculoskeletalExam", 
        "Neck", 
        "Neuro", 
        "Nose", 
        "Skin", 
        "Throat", 
        "VitalSign"
      ], 
      "label": "Physical Exam", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEnumeration"
      ], 
      "url": "http://schema.org/PhysicalExam"
    }, 
    "PhysicalTherapy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A process of progressive physical care and rehabilitation aimed at improving a health condition.", 
      "comment_plain": "A process of progressive physical care and rehabilitation aimed at improving a health condition.", 
      "id": "PhysicalTherapy", 
      "label": "Physical Therapy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/PhysicalTherapy"
    }, 
    "Physician": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A doctor's office.", 
      "comment_plain": "A doctor's office.", 
      "id": "Physician", 
      "label": "Physician", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "availableService", 
        "hospitalAffiliation", 
        "medicalSpecialty"
      ], 
      "specific_properties": [
        "availableService", 
        "hospitalAffiliation", 
        "medicalSpecialty"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/Physician"
    }, 
    "Place": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "Entities that have a somewhat fixed, physical extension.", 
      "comment_plain": "Entities that have a somewhat fixed, physical extension.", 
      "id": "Place", 
      "label": "Place", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "subtypes": [
        "AdministrativeArea", 
        "CivicStructure", 
        "Landform", 
        "LandmarksOrHistoricalBuildings", 
        "LocalBusiness", 
        "Residence", 
        "TouristAttraction"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Place"
    }, 
    "PlaceOfWorship": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "Place of worship, such as a church, synagogue, or mosque.", 
      "comment_plain": "Place of worship, such as a church, synagogue, or mosque.", 
      "id": "PlaceOfWorship", 
      "label": "Place of Worship", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BuddhistTemple", 
        "CatholicChurch", 
        "Church", 
        "HinduTemple", 
        "Mosque", 
        "Synagogue"
      ], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/PlaceOfWorship"
    }, 
    "Playground": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A playground.", 
      "comment_plain": "A playground.", 
      "id": "Playground", 
      "label": "Playground", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Playground"
    }, 
    "Plumber": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A plumbing service.", 
      "comment_plain": "A plumbing service.", 
      "id": "Plumber", 
      "label": "Plumber", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/Plumber"
    }, 
    "PoliceStation": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A police station.", 
      "comment_plain": "A police station.", 
      "id": "PoliceStation", 
      "label": "Police Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure", 
        "EmergencyService"
      ], 
      "url": "http://schema.org/PoliceStation"
    }, 
    "Pond": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A pond", 
      "comment_plain": "A pond", 
      "id": "Pond", 
      "label": "Pond", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/Pond"
    }, 
    "PostOffice": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "GovernmentOffice"
      ], 
      "comment": "A post office.", 
      "comment_plain": "A post office.", 
      "id": "PostOffice", 
      "label": "Post Office", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "GovernmentOffice"
      ], 
      "url": "http://schema.org/PostOffice"
    }, 
    "PostalAddress": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue", 
        "ContactPoint"
      ], 
      "comment": "The mailing address.", 
      "comment_plain": "The mailing address.", 
      "id": "PostalAddress", 
      "label": "Postal Address", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "contactType", 
        "email", 
        "faxNumber", 
        "telephone", 
        "addressCountry", 
        "addressLocality", 
        "addressRegion", 
        "postalCode", 
        "postOfficeBoxNumber", 
        "streetAddress"
      ], 
      "specific_properties": [
        "addressCountry", 
        "addressLocality", 
        "addressRegion", 
        "postalCode", 
        "postOfficeBoxNumber", 
        "streetAddress"
      ], 
      "subtypes": [], 
      "supertypes": [
        "ContactPoint"
      ], 
      "url": "http://schema.org/PostalAddress"
    }, 
    "Preschool": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "A preschool.", 
      "comment_plain": "A preschool.", 
      "id": "Preschool", 
      "label": "Preschool", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/Preschool"
    }, 
    "PreventionIndication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIndication"
      ], 
      "comment": "An indication for preventing an underlying condition, symptom, etc.", 
      "comment_plain": "An indication for preventing an underlying condition, symptom, etc.", 
      "id": "PreventionIndication", 
      "label": "Prevention Indication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIndication"
      ], 
      "url": "http://schema.org/PreventionIndication"
    }, 
    "PriceSpecification": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A structured value representing a monetary amount. Typically, only the subclasses of this type are used for markup.", 
      "comment_plain": "A structured value representing a monetary amount. Typically, only the subclasses of this type are used for markup.", 
      "id": "PriceSpecification", 
      "label": "Price Specification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "eligibleQuantity", 
        "eligibleTransactionVolume", 
        "maxPrice", 
        "minPrice", 
        "price", 
        "priceCurrency", 
        "validFrom", 
        "validThrough", 
        "valueAddedTaxIncluded"
      ], 
      "specific_properties": [
        "eligibleQuantity", 
        "eligibleTransactionVolume", 
        "maxPrice", 
        "minPrice", 
        "price", 
        "priceCurrency", 
        "validFrom", 
        "validThrough", 
        "valueAddedTaxIncluded"
      ], 
      "subtypes": [
        "DeliveryChargeSpecification", 
        "PaymentChargeSpecification", 
        "UnitPriceSpecification"
      ], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/PriceSpecification"
    }, 
    "Product": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "A product is anything that is made available for sale\u2014for example, a pair of shoes, a concert ticket, or a car. Commodity services, like haircuts, can also be represented using this type.", 
      "comment_plain": "A product is anything that is made available for sale\u2014for example, a pair of shoes, a concert ticket, or a car. Commodity services, like haircuts, can also be represented using this type.", 
      "id": "Product", 
      "label": "Product", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "aggregateRating", 
        "audience", 
        "brand", 
        "color", 
        "depth", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "height", 
        "isAccessoryOrSparePartFor", 
        "isConsumableFor", 
        "isRelatedTo", 
        "isSimilarTo", 
        "itemCondition", 
        "logo", 
        "manufacturer", 
        "model", 
        "mpn", 
        "offers", 
        "productID", 
        "releaseDate", 
        "review", 
        "reviews", 
        "sku", 
        "weight", 
        "width"
      ], 
      "specific_properties": [
        "aggregateRating", 
        "audience", 
        "brand", 
        "color", 
        "depth", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "height", 
        "isAccessoryOrSparePartFor", 
        "isConsumableFor", 
        "isRelatedTo", 
        "isSimilarTo", 
        "itemCondition", 
        "logo", 
        "manufacturer", 
        "model", 
        "mpn", 
        "offers", 
        "productID", 
        "releaseDate", 
        "review", 
        "reviews", 
        "sku", 
        "weight", 
        "width"
      ], 
      "subtypes": [
        "IndividualProduct", 
        "ProductModel", 
        "SomeProducts"
      ], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Product"
    }, 
    "ProductModel": {
      "ancestors": [
        "Thing", 
        "Product"
      ], 
      "comment": "A datasheet or vendor specification of a product (in the sense of a prototypical description).", 
      "comment_plain": "A datasheet or vendor specification of a product (in the sense of a prototypical description).", 
      "id": "ProductModel", 
      "label": "Product Model", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "aggregateRating", 
        "audience", 
        "brand", 
        "color", 
        "depth", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "height", 
        "isAccessoryOrSparePartFor", 
        "isConsumableFor", 
        "isRelatedTo", 
        "isSimilarTo", 
        "itemCondition", 
        "logo", 
        "manufacturer", 
        "model", 
        "mpn", 
        "offers", 
        "productID", 
        "releaseDate", 
        "review", 
        "reviews", 
        "sku", 
        "weight", 
        "width", 
        "isVariantOf", 
        "predecessorOf", 
        "successorOf"
      ], 
      "specific_properties": [
        "isVariantOf", 
        "predecessorOf", 
        "successorOf"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Product"
      ], 
      "url": "http://schema.org/ProductModel"
    }, 
    "ProfessionalService": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Provider of professional services.", 
      "comment_plain": "Provider of professional services.", 
      "id": "ProfessionalService", 
      "label": "Professional Service", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AccountingService", 
        "Attorney", 
        "Dentist", 
        "Electrician", 
        "GeneralContractor", 
        "HousePainter", 
        "Locksmith", 
        "Notary", 
        "Plumber", 
        "RoofingContractor"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/ProfessionalService"
    }, 
    "ProfilePage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: Profile page.", 
      "comment_plain": "Web page type: Profile page.", 
      "id": "ProfilePage", 
      "label": "Profile Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/ProfilePage"
    }, 
    "Property": {
      "ancestors": [
        "Thing"
      ], 
      "comment": "A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.", 
      "comment_plain": "A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.", 
      "id": "Property", 
      "label": "Property", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "domainIncludes", 
        "rangeIncludes"
      ], 
      "specific_properties": [
        "domainIncludes", 
        "rangeIncludes"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Thing"
      ], 
      "url": "http://schema.org/Property"
    }, 
    "PsychologicalTreatment": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A process of care relying upon counseling, dialogue, communication, verbalization aimed at improving a mental health condition.", 
      "comment_plain": "A process of care relying upon counseling, dialogue, communication, verbalization aimed at improving a mental health condition.", 
      "id": "PsychologicalTreatment", 
      "label": "Psychological Treatment", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/PsychologicalTreatment"
    }, 
    "PublicSwimmingPool": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A public swimming pool.", 
      "comment_plain": "A public swimming pool.", 
      "id": "PublicSwimmingPool", 
      "label": "Public Swimming Pool", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/PublicSwimmingPool"
    }, 
    "QualitativeValue": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A predefined value for a product characteristic, e.g. the the power cord plug type \"US\" or the garment sizes \"S\", \"M\", \"L\", and \"XL\"", 
      "comment_plain": "A predefined value for a product characteristic, e.g. the the power cord plug type \"US\" or the garment sizes \"S\", \"M\", \"L\", and \"XL\"", 
      "id": "QualitativeValue", 
      "label": "Qualitative Value", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "equal", 
        "greater", 
        "greaterOrEqual", 
        "lesser", 
        "lesserOrEqual", 
        "nonEqual", 
        "valueReference"
      ], 
      "specific_properties": [
        "equal", 
        "greater", 
        "greaterOrEqual", 
        "lesser", 
        "lesserOrEqual", 
        "nonEqual", 
        "valueReference"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/QualitativeValue"
    }, 
    "QuantitativeValue": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A point value or interval for product characteristics and other purposes.", 
      "comment_plain": "A point value or interval for product characteristics and other purposes.", 
      "id": "QuantitativeValue", 
      "label": "Quantitative Value", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "maxValue", 
        "minValue", 
        "unitCode", 
        "value", 
        "valueReference"
      ], 
      "specific_properties": [
        "maxValue", 
        "minValue", 
        "unitCode", 
        "value", 
        "valueReference"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/QuantitativeValue"
    }, 
    "Quantity": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.", 
      "comment_plain": "Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.", 
      "id": "Quantity", 
      "label": "Quantity", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Distance", 
        "Duration", 
        "Energy", 
        "Mass"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Quantity"
    }, 
    "RVPark": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "An RV park.", 
      "comment_plain": "An RV park.", 
      "id": "RVPark", 
      "label": "RV Park", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/RVPark"
    }, 
    "RadiationTherapy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalTherapy"
      ], 
      "comment": "A process of care using radiation aimed at improving a health condition.", 
      "comment_plain": "A process of care using radiation aimed at improving a health condition.", 
      "id": "RadiationTherapy", 
      "label": "Radiation Therapy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/RadiationTherapy"
    }, 
    "RadioStation": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A radio station.", 
      "comment_plain": "A radio station.", 
      "id": "RadioStation", 
      "label": "Radio Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/RadioStation"
    }, 
    "Rating": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "The rating of the video.", 
      "comment_plain": "The rating of the video.", 
      "id": "Rating", 
      "label": "Rating", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "bestRating", 
        "ratingValue", 
        "worstRating"
      ], 
      "specific_properties": [
        "bestRating", 
        "ratingValue", 
        "worstRating"
      ], 
      "subtypes": [
        "AggregateRating"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/Rating"
    }, 
    "RealEstateAgent": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A real-estate agent.", 
      "comment_plain": "A real-estate agent.", 
      "id": "RealEstateAgent", 
      "label": "Real Estate Agent", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/RealEstateAgent"
    }, 
    "Recipe": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A recipe.", 
      "comment_plain": "A recipe.", 
      "id": "Recipe", 
      "label": "Recipe", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "cookingMethod", 
        "cookTime", 
        "ingredients", 
        "nutrition", 
        "prepTime", 
        "recipeCategory", 
        "recipeCuisine", 
        "recipeInstructions", 
        "recipeYield", 
        "totalTime"
      ], 
      "specific_properties": [
        "cookingMethod", 
        "cookTime", 
        "ingredients", 
        "nutrition", 
        "prepTime", 
        "recipeCategory", 
        "recipeCuisine", 
        "recipeInstructions", 
        "recipeYield", 
        "totalTime"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Recipe"
    }, 
    "RecommendedDoseSchedule": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "DoseSchedule"
      ], 
      "comment": "A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.", 
      "comment_plain": "A recommended dosing schedule for a drug or supplement as prescribed or recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.", 
      "id": "RecommendedDoseSchedule", 
      "label": "Recommended Dose Schedule", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "doseUnit", 
        "doseValue", 
        "frequency", 
        "targetPopulation"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DoseSchedule"
      ], 
      "url": "http://schema.org/RecommendedDoseSchedule"
    }, 
    "RecyclingCenter": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A recycling center.", 
      "comment_plain": "A recycling center.", 
      "id": "RecyclingCenter", 
      "label": "Recycling Center", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/RecyclingCenter"
    }, 
    "ReportedDoseSchedule": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIntangible", 
        "DoseSchedule"
      ], 
      "comment": "A patient-reported or observed dosing schedule for a drug or supplement.", 
      "comment_plain": "A patient-reported or observed dosing schedule for a drug or supplement.", 
      "id": "ReportedDoseSchedule", 
      "label": "Reported Dose Schedule", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "doseUnit", 
        "doseValue", 
        "frequency", 
        "targetPopulation"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "DoseSchedule"
      ], 
      "url": "http://schema.org/ReportedDoseSchedule"
    }, 
    "Reservoir": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A reservoir, like the Lake Kariba reservoir.", 
      "comment_plain": "A reservoir, like the Lake Kariba reservoir.", 
      "id": "Reservoir", 
      "label": "Reservoir", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/Reservoir"
    }, 
    "Residence": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "The place where a person lives.", 
      "comment_plain": "The place where a person lives.", 
      "id": "Residence", 
      "label": "Residence", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "ApartmentComplex", 
        "GatedResidenceCommunity", 
        "SingleFamilyResidence"
      ], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/Residence"
    }, 
    "Restaurant": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A restaurant.", 
      "comment_plain": "A restaurant.", 
      "id": "Restaurant", 
      "label": "Restaurant", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/Restaurant"
    }, 
    "Review": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A review of an item - for example, a restaurant, movie, or store.", 
      "comment_plain": "A review of an item - for example, a restaurant, movie, or store.", 
      "id": "Review", 
      "label": "Review", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "itemReviewed", 
        "reviewBody", 
        "reviewRating"
      ], 
      "specific_properties": [
        "itemReviewed", 
        "reviewBody", 
        "reviewRating"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Review"
    }, 
    "RiverBodyOfWater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A river (for example, the broad majestic Shannon).", 
      "comment_plain": "A river (for example, the broad majestic Shannon).", 
      "id": "RiverBodyOfWater", 
      "label": "River Body of Water", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/RiverBodyOfWater"
    }, 
    "RoofingContractor": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HomeAndConstructionBusiness"
      ], 
      "comment": "A roofing contractor.", 
      "comment_plain": "A roofing contractor.", 
      "id": "RoofingContractor", 
      "label": "Roofing Contractor", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "ProfessionalService", 
        "HomeAndConstructionBusiness"
      ], 
      "url": "http://schema.org/RoofingContractor"
    }, 
    "SaleEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Sales event.", 
      "comment_plain": "Event type: Sales event.", 
      "id": "SaleEvent", 
      "label": "Sale Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/SaleEvent"
    }, 
    "ScholarlyArticle": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article"
      ], 
      "comment": "A scholarly article.", 
      "comment_plain": "A scholarly article.", 
      "id": "ScholarlyArticle", 
      "label": "Scholarly Article", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "MedicalScholarlyArticle"
      ], 
      "supertypes": [
        "Article"
      ], 
      "url": "http://schema.org/ScholarlyArticle"
    }, 
    "School": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "EducationalOrganization"
      ], 
      "comment": "A school.", 
      "comment_plain": "A school.", 
      "id": "School", 
      "label": "School", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID", 
        "alumni"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "EducationalOrganization"
      ], 
      "url": "http://schema.org/School"
    }, 
    "Sculpture": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A piece of sculpture.", 
      "comment_plain": "A piece of sculpture.", 
      "id": "Sculpture", 
      "label": "Sculpture", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/Sculpture"
    }, 
    "SeaBodyOfWater": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A sea (for example, the Caspian sea).", 
      "comment_plain": "A sea (for example, the Caspian sea).", 
      "id": "SeaBodyOfWater", 
      "label": "Sea Body of Water", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/SeaBodyOfWater"
    }, 
    "SearchResultsPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage"
      ], 
      "comment": "Web page type: Search results page.", 
      "comment_plain": "Web page type: Search results page.", 
      "id": "SearchResultsPage", 
      "label": "Search Results Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPage"
      ], 
      "url": "http://schema.org/SearchResultsPage"
    }, 
    "SelfStorage": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "Self-storage facility.", 
      "comment_plain": "Self-storage facility.", 
      "id": "SelfStorage", 
      "label": "Self Storage", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/SelfStorage"
    }, 
    "ShoeStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A shoe store.", 
      "comment_plain": "A shoe store.", 
      "id": "ShoeStore", 
      "label": "Shoe Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ShoeStore"
    }, 
    "ShoppingCenter": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A shopping center or mall.", 
      "comment_plain": "A shopping center or mall.", 
      "id": "ShoppingCenter", 
      "label": "Shopping Center", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/ShoppingCenter"
    }, 
    "SingleFamilyResidence": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Residence"
      ], 
      "comment": "Residence type: Single-family home.", 
      "comment_plain": "Residence type: Single-family home.", 
      "id": "SingleFamilyResidence", 
      "label": "Single Family Residence", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Residence"
      ], 
      "url": "http://schema.org/SingleFamilyResidence"
    }, 
    "SiteNavigationElement": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "A navigation element of the page.", 
      "comment_plain": "A navigation element of the page.", 
      "id": "SiteNavigationElement", 
      "label": "Site Navigation Element", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/SiteNavigationElement"
    }, 
    "SkiResort": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A ski resort.", 
      "comment_plain": "A ski resort.", 
      "id": "SkiResort", 
      "label": "Ski Resort", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/SkiResort"
    }, 
    "SocialEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Social event.", 
      "comment_plain": "Event type: Social event.", 
      "id": "SocialEvent", 
      "label": "Social Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/SocialEvent"
    }, 
    "SoftwareApplication": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A software application.", 
      "comment_plain": "A software application.", 
      "id": "SoftwareApplication", 
      "label": "Software Application", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "applicationCategory", 
        "applicationSubCategory", 
        "applicationSuite", 
        "countriesNotSupported", 
        "countriesSupported", 
        "device", 
        "downloadUrl", 
        "featureList", 
        "fileFormat", 
        "fileSize", 
        "installUrl", 
        "memoryRequirements", 
        "operatingSystem", 
        "permissions", 
        "processorRequirements", 
        "releaseNotes", 
        "requirements", 
        "screenshot", 
        "softwareVersion", 
        "storageRequirements"
      ], 
      "specific_properties": [
        "applicationCategory", 
        "applicationSubCategory", 
        "applicationSuite", 
        "countriesNotSupported", 
        "countriesSupported", 
        "device", 
        "downloadUrl", 
        "featureList", 
        "fileFormat", 
        "fileSize", 
        "installUrl", 
        "memoryRequirements", 
        "operatingSystem", 
        "permissions", 
        "processorRequirements", 
        "releaseNotes", 
        "requirements", 
        "screenshot", 
        "softwareVersion", 
        "storageRequirements"
      ], 
      "subtypes": [
        "MobileApplication", 
        "WebApplication"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/SoftwareApplication"
    }, 
    "SomeProducts": {
      "ancestors": [
        "Thing", 
        "Product"
      ], 
      "comment": "A placeholder for multiple similar products of the same kind.", 
      "comment_plain": "A placeholder for multiple similar products of the same kind.", 
      "id": "SomeProducts", 
      "label": "Some Products", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "aggregateRating", 
        "audience", 
        "brand", 
        "color", 
        "depth", 
        "gtin13", 
        "gtin14", 
        "gtin8", 
        "height", 
        "isAccessoryOrSparePartFor", 
        "isConsumableFor", 
        "isRelatedTo", 
        "isSimilarTo", 
        "itemCondition", 
        "logo", 
        "manufacturer", 
        "model", 
        "mpn", 
        "offers", 
        "productID", 
        "releaseDate", 
        "review", 
        "reviews", 
        "sku", 
        "weight", 
        "width", 
        "inventoryLevel"
      ], 
      "specific_properties": [
        "inventoryLevel"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Product"
      ], 
      "url": "http://schema.org/SomeProducts"
    }, 
    "Specialty": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.", 
      "comment_plain": "Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.", 
      "id": "Specialty", 
      "label": "Specialty", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "MedicalSpecialty"
      ], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/Specialty"
    }, 
    "SportingGoodsStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A sporting goods store.", 
      "comment_plain": "A sporting goods store.", 
      "id": "SportingGoodsStore", 
      "label": "Sporting Goods Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/SportingGoodsStore"
    }, 
    "SportsActivityLocation": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A sports location, such as a playing field.", 
      "comment_plain": "A sports location, such as a playing field.", 
      "id": "SportsActivityLocation", 
      "label": "Sports Activity Location", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "BowlingAlley", 
        "ExerciseGym", 
        "GolfCourse", 
        "HealthClub", 
        "PublicSwimmingPool", 
        "SkiResort", 
        "SportsClub", 
        "StadiumOrArena", 
        "TennisComplex"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/SportsActivityLocation"
    }, 
    "SportsClub": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A sports club.", 
      "comment_plain": "A sports club.", 
      "id": "SportsClub", 
      "label": "Sports Club", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/SportsClub"
    }, 
    "SportsEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Sports event.", 
      "comment_plain": "Event type: Sports event.", 
      "id": "SportsEvent", 
      "label": "Sports Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/SportsEvent"
    }, 
    "SportsTeam": {
      "ancestors": [
        "Thing", 
        "Organization"
      ], 
      "comment": "Organization: Sports team.", 
      "comment_plain": "Organization: Sports team.", 
      "id": "SportsTeam", 
      "label": "Sports Team", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Organization"
      ], 
      "url": "http://schema.org/SportsTeam"
    }, 
    "StadiumOrArena": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A stadium.", 
      "comment_plain": "A stadium.", 
      "id": "StadiumOrArena", 
      "label": "Stadium or Arena", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure", 
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/StadiumOrArena"
    }, 
    "State": {
      "ancestors": [
        "Thing", 
        "Place", 
        "AdministrativeArea"
      ], 
      "comment": "A state or province.", 
      "comment_plain": "A state or province.", 
      "id": "State", 
      "label": "State", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "AdministrativeArea"
      ], 
      "url": "http://schema.org/State"
    }, 
    "Store": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A retail good store.", 
      "comment_plain": "A retail good store.", 
      "id": "Store", 
      "label": "Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "AutoPartsStore", 
        "BikeStore", 
        "BookStore", 
        "ClothingStore", 
        "ComputerStore", 
        "ConvenienceStore", 
        "DepartmentStore", 
        "ElectronicsStore", 
        "Florist", 
        "FurnitureStore", 
        "GardenStore", 
        "GroceryStore", 
        "HardwareStore", 
        "HobbyShop", 
        "HomeGoodsStore", 
        "JewelryStore", 
        "LiquorStore", 
        "MensClothingStore", 
        "MobilePhoneStore", 
        "MovieRentalStore", 
        "MusicStore", 
        "OfficeEquipmentStore", 
        "OutletStore", 
        "PawnShop", 
        "PetStore", 
        "ShoeStore", 
        "SportingGoodsStore", 
        "TireShop", 
        "ToyStore", 
        "WholesaleStore"
      ], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/Store"
    }, 
    "StructuredValue": {
      "ancestors": [
        "Thing", 
        "Intangible"
      ], 
      "comment": "Structured values are strings\u2014for example, addresses\u2014that have certain constraints on their structure.", 
      "comment_plain": "Structured values are strings\u2014for example, addresses\u2014that have certain constraints on their structure.", 
      "id": "StructuredValue", 
      "label": "Structured Value", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "ContactPoint", 
        "GeoCoordinates", 
        "GeoShape", 
        "NutritionInformation", 
        "OpeningHoursSpecification", 
        "OwnershipInfo", 
        "PriceSpecification", 
        "QuantitativeValue", 
        "TypeAndQuantityNode", 
        "WarrantyPromise"
      ], 
      "supertypes": [
        "Intangible"
      ], 
      "url": "http://schema.org/StructuredValue"
    }, 
    "SubwayStation": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A subway station.", 
      "comment_plain": "A subway station.", 
      "id": "SubwayStation", 
      "label": "Subway Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/SubwayStation"
    }, 
    "SuperficialAnatomy": {
      "ancestors": [
        "Thing", 
        "MedicalEntity"
      ], 
      "comment": "Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).", 
      "comment_plain": "Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).", 
      "id": "SuperficialAnatomy", 
      "label": "Superficial Anatomy", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "relatedAnatomy", 
        "relatedCondition", 
        "relatedTherapy", 
        "significance"
      ], 
      "specific_properties": [
        "associatedPathophysiology", 
        "relatedAnatomy", 
        "relatedCondition", 
        "relatedTherapy", 
        "significance"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MedicalEntity"
      ], 
      "url": "http://schema.org/SuperficialAnatomy"
    }, 
    "Synagogue": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure", 
        "PlaceOfWorship"
      ], 
      "comment": "A synagogue.", 
      "comment_plain": "A synagogue.", 
      "id": "Synagogue", 
      "label": "Synagogue", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PlaceOfWorship"
      ], 
      "url": "http://schema.org/Synagogue"
    }, 
    "TVEpisode": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "An episode of a TV series or season.", 
      "comment_plain": "An episode of a TV series or season.", 
      "id": "TVEpisode", 
      "label": "TV Episode", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "actor", 
        "actors", 
        "director", 
        "episodeNumber", 
        "musicBy", 
        "partOfSeason", 
        "partOfTVSeries", 
        "producer", 
        "productionCompany", 
        "trailer"
      ], 
      "specific_properties": [
        "actor", 
        "actors", 
        "director", 
        "episodeNumber", 
        "musicBy", 
        "partOfSeason", 
        "partOfTVSeries", 
        "producer", 
        "productionCompany", 
        "trailer"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/TVEpisode"
    }, 
    "TVSeason": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A TV season.", 
      "comment_plain": "A TV season.", 
      "id": "TVSeason", 
      "label": "TV Season", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "endDate", 
        "episode", 
        "episodes", 
        "numberOfEpisodes", 
        "partOfTVSeries", 
        "seasonNumber", 
        "startDate", 
        "trailer"
      ], 
      "specific_properties": [
        "endDate", 
        "episode", 
        "episodes", 
        "numberOfEpisodes", 
        "partOfTVSeries", 
        "seasonNumber", 
        "startDate", 
        "trailer"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/TVSeason"
    }, 
    "TVSeries": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A television series.", 
      "comment_plain": "A television series.", 
      "id": "TVSeries", 
      "label": "TV Series", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "actor", 
        "actors", 
        "director", 
        "endDate", 
        "episode", 
        "episodes", 
        "musicBy", 
        "numberOfEpisodes", 
        "producer", 
        "productionCompany", 
        "season", 
        "seasons", 
        "startDate", 
        "trailer"
      ], 
      "specific_properties": [
        "actor", 
        "actors", 
        "director", 
        "endDate", 
        "episode", 
        "episodes", 
        "musicBy", 
        "numberOfEpisodes", 
        "producer", 
        "productionCompany", 
        "season", 
        "seasons", 
        "startDate", 
        "trailer"
      ], 
      "subtypes": [], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/TVSeries"
    }, 
    "Table": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "A table on the page.", 
      "comment_plain": "A table on the page.", 
      "id": "Table", 
      "label": "Table", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/Table"
    }, 
    "TattooParlor": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "HealthAndBeautyBusiness"
      ], 
      "comment": "A tattoo parlor.", 
      "comment_plain": "A tattoo parlor.", 
      "id": "TattooParlor", 
      "label": "Tattoo Parlor", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "HealthAndBeautyBusiness"
      ], 
      "url": "http://schema.org/TattooParlor"
    }, 
    "TaxiStand": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A taxi stand.", 
      "comment_plain": "A taxi stand.", 
      "id": "TaxiStand", 
      "label": "Taxi Stand", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/TaxiStand"
    }, 
    "TechArticle": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "Article"
      ], 
      "comment": "A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.", 
      "comment_plain": "A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.", 
      "id": "TechArticle", 
      "label": "Tech Article", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "articleBody", 
        "articleSection", 
        "wordCount", 
        "dependencies", 
        "proficiencyLevel"
      ], 
      "specific_properties": [
        "dependencies", 
        "proficiencyLevel"
      ], 
      "subtypes": [
        "APIReference"
      ], 
      "supertypes": [
        "Article"
      ], 
      "url": "http://schema.org/TechArticle"
    }, 
    "TelevisionStation": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A television station.", 
      "comment_plain": "A television station.", 
      "id": "TelevisionStation", 
      "label": "Television Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/TelevisionStation"
    }, 
    "TennisComplex": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "SportsActivityLocation"
      ], 
      "comment": "A tennis complex.", 
      "comment_plain": "A tennis complex.", 
      "id": "TennisComplex", 
      "label": "Tennis Complex", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "SportsActivityLocation"
      ], 
      "url": "http://schema.org/TennisComplex"
    }, 
    "TheaterEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Theater performance.", 
      "comment_plain": "Event type: Theater performance.", 
      "id": "TheaterEvent", 
      "label": "Theater Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/TheaterEvent"
    }, 
    "TheaterGroup": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "PerformingGroup"
      ], 
      "comment": "A theater group or company\u2014for example, the Royal Shakespeare Company or Druid Theatre.", 
      "comment_plain": "A theater group or company\u2014for example, the Royal Shakespeare Company or Druid Theatre.", 
      "id": "TheaterGroup", 
      "label": "Theater Group", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "event", 
        "events", 
        "faxNumber", 
        "founder", 
        "founders", 
        "foundingDate", 
        "globalLocationNumber", 
        "hasPOS", 
        "interactionCount", 
        "isicV4", 
        "legalName", 
        "location", 
        "logo", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "review", 
        "reviews", 
        "seeks", 
        "taxID", 
        "telephone", 
        "vatID"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "PerformingGroup"
      ], 
      "url": "http://schema.org/TheaterGroup"
    }, 
    "TherapeuticProcedure": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalProcedure"
      ], 
      "comment": "A medical procedure intended primarly for therapeutic purposes, aimed at improving a health condition.", 
      "comment_plain": "A medical procedure intended primarly for therapeutic purposes, aimed at improving a health condition.", 
      "id": "TherapeuticProcedure", 
      "label": "Therapeutic Procedure", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "adverseOutcome", 
        "contraindication", 
        "duplicateTherapy", 
        "indication", 
        "seriousAdverseOutcome", 
        "followup", 
        "howPerformed", 
        "preparation", 
        "procedureType"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalProcedure", 
        "MedicalTherapy"
      ], 
      "url": "http://schema.org/TherapeuticProcedure"
    }, 
    "Thing": {
      "ancestors": [], 
      "comment": "The most generic type of item.", 
      "comment_plain": "The most generic type of item.", 
      "id": "Thing", 
      "label": "Thing", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "subtypes": [
        "Class", 
        "CreativeWork", 
        "Event", 
        "Intangible", 
        "MedicalEntity", 
        "Organization", 
        "Person", 
        "Place", 
        "Product", 
        "Property"
      ], 
      "supertypes": [], 
      "url": "http://schema.org/Thing"
    }, 
    "TireShop": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A tire shop.", 
      "comment_plain": "A tire shop.", 
      "id": "TireShop", 
      "label": "Tire Shop", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/TireShop"
    }, 
    "TouristAttraction": {
      "ancestors": [
        "Thing", 
        "Place"
      ], 
      "comment": "A tourist attraction.", 
      "comment_plain": "A tourist attraction.", 
      "id": "TouristAttraction", 
      "label": "Tourist Attraction", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Place"
      ], 
      "url": "http://schema.org/TouristAttraction"
    }, 
    "TouristInformationCenter": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A tourist information center.", 
      "comment_plain": "A tourist information center.", 
      "id": "TouristInformationCenter", 
      "label": "Tourist Information Center", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/TouristInformationCenter"
    }, 
    "ToyStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A toystore.", 
      "comment_plain": "A toystore.", 
      "id": "ToyStore", 
      "label": "Toy Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/ToyStore"
    }, 
    "TrainStation": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A train station.", 
      "comment_plain": "A train station.", 
      "id": "TrainStation", 
      "label": "Train Station", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/TrainStation"
    }, 
    "TravelAgency": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness"
      ], 
      "comment": "A travel agency.", 
      "comment_plain": "A travel agency.", 
      "id": "TravelAgency", 
      "label": "Travel Agency", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "LocalBusiness"
      ], 
      "url": "http://schema.org/TravelAgency"
    }, 
    "TreatmentIndication": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "MedicalIndication"
      ], 
      "comment": "An indication for treating an underlying condition, symptom, etc.", 
      "comment_plain": "An indication for treating an underlying condition, symptom, etc.", 
      "id": "TreatmentIndication", 
      "label": "Treatment Indication", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalIndication"
      ], 
      "url": "http://schema.org/TreatmentIndication"
    }, 
    "TypeAndQuantityNode": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.", 
      "comment_plain": "A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.", 
      "id": "TypeAndQuantityNode", 
      "label": "Type And Quantity Node", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "amountOfThisGood", 
        "businessFunction", 
        "typeOfGood", 
        "unitCode"
      ], 
      "specific_properties": [
        "amountOfThisGood", 
        "businessFunction", 
        "typeOfGood", 
        "unitCode"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/TypeAndQuantityNode"
    }, 
    "UnitPriceSpecification": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue", 
        "PriceSpecification"
      ], 
      "comment": "The price asked for a given offer by the respective organization or person.", 
      "comment_plain": "The price asked for a given offer by the respective organization or person.", 
      "id": "UnitPriceSpecification", 
      "label": "Unit Price Specification", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "eligibleQuantity", 
        "eligibleTransactionVolume", 
        "maxPrice", 
        "minPrice", 
        "price", 
        "priceCurrency", 
        "validFrom", 
        "validThrough", 
        "valueAddedTaxIncluded", 
        "billingIncrement", 
        "priceType", 
        "unitCode"
      ], 
      "specific_properties": [
        "billingIncrement", 
        "priceType", 
        "unitCode"
      ], 
      "subtypes": [], 
      "supertypes": [
        "PriceSpecification"
      ], 
      "url": "http://schema.org/UnitPriceSpecification"
    }, 
    "UserBlocks": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Block this content.", 
      "comment_plain": "User interaction: Block this content.", 
      "id": "UserBlocks", 
      "label": "User Blocks", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserBlocks"
    }, 
    "UserCheckins": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Check-in at a place.", 
      "comment_plain": "User interaction: Check-in at a place.", 
      "id": "UserCheckins", 
      "label": "User Checkins", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserCheckins"
    }, 
    "UserComments": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "The UserInteraction event in which a user comments on an item.", 
      "comment_plain": "The UserInteraction event in which a user comments on an item.", 
      "id": "UserComments", 
      "label": "User Comments", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent", 
        "commentText", 
        "commentTime", 
        "creator", 
        "discusses", 
        "replyToUrl"
      ], 
      "specific_properties": [
        "commentText", 
        "commentTime", 
        "creator", 
        "discusses", 
        "replyToUrl"
      ], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserComments"
    }, 
    "UserDownloads": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Download of an item.", 
      "comment_plain": "User interaction: Download of an item.", 
      "id": "UserDownloads", 
      "label": "User Downloads", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserDownloads"
    }, 
    "UserInteraction": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "A user interacting with a page", 
      "comment_plain": "A user interacting with a page", 
      "id": "UserInteraction", 
      "label": "User Interaction", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "UserBlocks", 
        "UserCheckins", 
        "UserComments", 
        "UserDownloads", 
        "UserLikes", 
        "UserPageVisits", 
        "UserPlays", 
        "UserPlusOnes", 
        "UserTweets"
      ], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/UserInteraction"
    }, 
    "UserLikes": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Like an item.", 
      "comment_plain": "User interaction: Like an item.", 
      "id": "UserLikes", 
      "label": "User Likes", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserLikes"
    }, 
    "UserPageVisits": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Visit to a web page.", 
      "comment_plain": "User interaction: Visit to a web page.", 
      "id": "UserPageVisits", 
      "label": "User Page Visits", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserPageVisits"
    }, 
    "UserPlays": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Play count of an item, for example a video or a song.", 
      "comment_plain": "User interaction: Play count of an item, for example a video or a song.", 
      "id": "UserPlays", 
      "label": "User Plays", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserPlays"
    }, 
    "UserPlusOnes": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: +1.", 
      "comment_plain": "User interaction: +1.", 
      "id": "UserPlusOnes", 
      "label": "User Plus Ones", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserPlusOnes"
    }, 
    "UserTweets": {
      "ancestors": [
        "Thing", 
        "Event", 
        "UserInteraction"
      ], 
      "comment": "User interaction: Tweets.", 
      "comment_plain": "User interaction: Tweets.", 
      "id": "UserTweets", 
      "label": "User Tweets", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "UserInteraction"
      ], 
      "url": "http://schema.org/UserTweets"
    }, 
    "Vein": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure", 
        "Vessel"
      ], 
      "comment": "A type of blood vessel that specifically carries blood to the heart.", 
      "comment_plain": "A type of blood vessel that specifically carries blood to the heart.", 
      "id": "Vein", 
      "label": "Vein", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure", 
        "drainsTo", 
        "regionDrained", 
        "tributary"
      ], 
      "specific_properties": [
        "drainsTo", 
        "regionDrained", 
        "tributary"
      ], 
      "subtypes": [], 
      "supertypes": [
        "Vessel"
      ], 
      "url": "http://schema.org/Vein"
    }, 
    "Vessel": {
      "ancestors": [
        "Thing", 
        "MedicalEntity", 
        "AnatomicalStructure"
      ], 
      "comment": "A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.", 
      "comment_plain": "A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.", 
      "id": "Vessel", 
      "label": "Vessel", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "alternateName", 
        "code", 
        "guideline", 
        "medicineSystem", 
        "recognizingAuthority", 
        "relevantSpecialty", 
        "study", 
        "associatedPathophysiology", 
        "bodyLocation", 
        "connectedTo", 
        "diagram", 
        "function", 
        "partOfSystem", 
        "relatedCondition", 
        "relatedTherapy", 
        "subStructure"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "Artery", 
        "LymphaticVessel", 
        "Vein"
      ], 
      "supertypes": [
        "AnatomicalStructure"
      ], 
      "url": "http://schema.org/Vessel"
    }, 
    "VeterinaryCare": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "MedicalOrganization"
      ], 
      "comment": "A vet's office.", 
      "comment_plain": "A vet's office.", 
      "id": "VeterinaryCare", 
      "label": "Veterinary Care", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "MedicalOrganization"
      ], 
      "url": "http://schema.org/VeterinaryCare"
    }, 
    "VideoGallery": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPage", 
        "CollectionPage"
      ], 
      "comment": "Web page type: Video gallery page.", 
      "comment_plain": "Web page type: Video gallery page.", 
      "id": "VideoGallery", 
      "label": "Video Gallery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CollectionPage"
      ], 
      "url": "http://schema.org/VideoGallery"
    }, 
    "VideoObject": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "MediaObject"
      ], 
      "comment": "A video file.", 
      "comment_plain": "A video file.", 
      "id": "VideoObject", 
      "label": "Video Object", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "associatedArticle", 
        "bitrate", 
        "contentSize", 
        "contentUrl", 
        "duration", 
        "embedUrl", 
        "encodesCreativeWork", 
        "encodingFormat", 
        "expires", 
        "height", 
        "playerType", 
        "regionsAllowed", 
        "requiresSubscription", 
        "uploadDate", 
        "width", 
        "caption", 
        "productionCompany", 
        "thumbnail", 
        "transcript", 
        "videoFrameSize", 
        "videoQuality"
      ], 
      "specific_properties": [
        "caption", 
        "productionCompany", 
        "thumbnail", 
        "transcript", 
        "videoFrameSize", 
        "videoQuality"
      ], 
      "subtypes": [], 
      "supertypes": [
        "MediaObject"
      ], 
      "url": "http://schema.org/VideoObject"
    }, 
    "VisualArtsEvent": {
      "ancestors": [
        "Thing", 
        "Event"
      ], 
      "comment": "Event type: Visual arts event.", 
      "comment_plain": "Event type: Visual arts event.", 
      "id": "VisualArtsEvent", 
      "label": "Visual Arts Event", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "attendee", 
        "attendees", 
        "duration", 
        "endDate", 
        "location", 
        "offers", 
        "performer", 
        "performers", 
        "startDate", 
        "subEvent", 
        "subEvents", 
        "superEvent"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Event"
      ], 
      "url": "http://schema.org/VisualArtsEvent"
    }, 
    "Volcano": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform"
      ], 
      "comment": "A volcano, like Fuji san", 
      "comment_plain": "A volcano, like Fuji san", 
      "id": "Volcano", 
      "label": "Volcano", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Landform"
      ], 
      "url": "http://schema.org/Volcano"
    }, 
    "WPAdBlock": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "An advertising section of the page.", 
      "comment_plain": "An advertising section of the page.", 
      "id": "WPAdBlock", 
      "label": "WP Ad Block", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/WPAdBlock"
    }, 
    "WPFooter": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "The footer section of the page.", 
      "comment_plain": "The footer section of the page.", 
      "id": "WPFooter", 
      "label": "WP Footer", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/WPFooter"
    }, 
    "WPHeader": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "The header section of the page.", 
      "comment_plain": "The header section of the page.", 
      "id": "WPHeader", 
      "label": "WP Header", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/WPHeader"
    }, 
    "WPSideBar": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "WebPageElement"
      ], 
      "comment": "A sidebar section of the page.", 
      "comment_plain": "A sidebar section of the page.", 
      "id": "WPSideBar", 
      "label": "WP Side Bar", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "WebPageElement"
      ], 
      "url": "http://schema.org/WPSideBar"
    }, 
    "WarrantyPromise": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "StructuredValue"
      ], 
      "comment": "A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.", 
      "comment_plain": "A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.", 
      "id": "WarrantyPromise", 
      "label": "Warranty Promise", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "durationOfWarranty", 
        "warrantyScope"
      ], 
      "specific_properties": [
        "durationOfWarranty", 
        "warrantyScope"
      ], 
      "subtypes": [], 
      "supertypes": [
        "StructuredValue"
      ], 
      "url": "http://schema.org/WarrantyPromise"
    }, 
    "WarrantyScope": {
      "ancestors": [
        "Thing", 
        "Intangible", 
        "Enumeration"
      ], 
      "comment": "A range of of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Labor-BringIn\nhttp://purl.org/goodrelations/v1#PartsAndLabor-BringIn\nhttp://purl.org/goodrelations/v1#PartsAndLabor-PickUp", 
      "comment_plain": "A range of of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\n\nCommonly used values:\n\nhttp://purl.org/goodrelations/v1#Labor-BringIn\nhttp://purl.org/goodrelations/v1#PartsAndLabor-BringIn\nhttp://purl.org/goodrelations/v1#PartsAndLabor-PickUp", 
      "id": "WarrantyScope", 
      "label": "Warranty Scope", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Enumeration"
      ], 
      "url": "http://schema.org/WarrantyScope"
    }, 
    "Waterfall": {
      "ancestors": [
        "Thing", 
        "Place", 
        "Landform", 
        "BodyOfWater"
      ], 
      "comment": "A waterfall, like Niagara", 
      "comment_plain": "A waterfall, like Niagara", 
      "id": "Waterfall", 
      "label": "Waterfall", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "BodyOfWater"
      ], 
      "url": "http://schema.org/Waterfall"
    }, 
    "WebApplication": {
      "ancestors": [
        "Thing", 
        "CreativeWork", 
        "SoftwareApplication"
      ], 
      "comment": "Web applications.", 
      "comment_plain": "Web applications.", 
      "id": "WebApplication", 
      "label": "Web Application", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "applicationCategory", 
        "applicationSubCategory", 
        "applicationSuite", 
        "countriesNotSupported", 
        "countriesSupported", 
        "device", 
        "downloadUrl", 
        "featureList", 
        "fileFormat", 
        "fileSize", 
        "installUrl", 
        "memoryRequirements", 
        "operatingSystem", 
        "permissions", 
        "processorRequirements", 
        "releaseNotes", 
        "requirements", 
        "screenshot", 
        "softwareVersion", 
        "storageRequirements", 
        "browserRequirements"
      ], 
      "specific_properties": [
        "browserRequirements"
      ], 
      "subtypes": [], 
      "supertypes": [
        "SoftwareApplication"
      ], 
      "url": "http://schema.org/WebApplication"
    }, 
    "WebPage": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page", 
      "comment_plain": "A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page", 
      "id": "WebPage", 
      "label": "Web Page", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video", 
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "specific_properties": [
        "breadcrumb", 
        "isPartOf", 
        "lastReviewed", 
        "mainContentOfPage", 
        "primaryImageOfPage", 
        "relatedLink", 
        "reviewedBy", 
        "significantLink", 
        "significantLinks", 
        "specialty"
      ], 
      "subtypes": [
        "AboutPage", 
        "CheckoutPage", 
        "CollectionPage", 
        "ContactPage", 
        "ItemPage", 
        "MedicalWebPage", 
        "ProfilePage", 
        "SearchResultsPage"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/WebPage"
    }, 
    "WebPageElement": {
      "ancestors": [
        "Thing", 
        "CreativeWork"
      ], 
      "comment": "A web page element, like a table or an image", 
      "comment_plain": "A web page element, like a table or an image", 
      "id": "WebPageElement", 
      "label": "Web Page Element", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "about", 
        "accountablePerson", 
        "aggregateRating", 
        "alternativeHeadline", 
        "associatedMedia", 
        "audience", 
        "audio", 
        "author", 
        "award", 
        "awards", 
        "comment", 
        "contentLocation", 
        "contentRating", 
        "contributor", 
        "copyrightHolder", 
        "copyrightYear", 
        "creator", 
        "dateCreated", 
        "dateModified", 
        "datePublished", 
        "discussionUrl", 
        "editor", 
        "educationalAlignment", 
        "educationalUse", 
        "encoding", 
        "encodings", 
        "genre", 
        "headline", 
        "inLanguage", 
        "interactionCount", 
        "interactivityType", 
        "isBasedOnUrl", 
        "isFamilyFriendly", 
        "keywords", 
        "learningResourceType", 
        "mentions", 
        "offers", 
        "provider", 
        "publisher", 
        "publishingPrinciples", 
        "review", 
        "reviews", 
        "sourceOrganization", 
        "text", 
        "thumbnailUrl", 
        "timeRequired", 
        "typicalAgeRange", 
        "version", 
        "video"
      ], 
      "specific_properties": [], 
      "subtypes": [
        "SiteNavigationElement", 
        "Table", 
        "WPAdBlock", 
        "WPFooter", 
        "WPHeader", 
        "WPSideBar"
      ], 
      "supertypes": [
        "CreativeWork"
      ], 
      "url": "http://schema.org/WebPageElement"
    }, 
    "WholesaleStore": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "Store"
      ], 
      "comment": "A wholesale store.", 
      "comment_plain": "A wholesale store.", 
      "id": "WholesaleStore", 
      "label": "Wholesale Store", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "Store"
      ], 
      "url": "http://schema.org/WholesaleStore"
    }, 
    "Winery": {
      "ancestors": [
        "Thing", 
        "Organization", 
        "LocalBusiness", 
        "FoodEstablishment"
      ], 
      "comment": "A winery.", 
      "comment_plain": "A winery.", 
      "id": "Winery", 
      "label": "Winery", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "brand", 
        "contactPoint", 
        "contactPoints", 
        "duns", 
        "email", 
        "employee", 
        "employees", 
        "founder", 
        "founders", 
        "foundingDate", 
        "hasPOS", 
        "legalName", 
        "location", 
        "makesOffer", 
        "member", 
        "members", 
        "naics", 
        "owns", 
        "seeks", 
        "taxID", 
        "vatID", 
        "branchOf", 
        "currenciesAccepted", 
        "openingHours", 
        "paymentAccepted", 
        "priceRange", 
        "acceptsReservations", 
        "menu", 
        "servesCuisine"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "FoodEstablishment"
      ], 
      "url": "http://schema.org/Winery"
    }, 
    "Zoo": {
      "ancestors": [
        "Thing", 
        "Place", 
        "CivicStructure"
      ], 
      "comment": "A zoo.", 
      "comment_plain": "A zoo.", 
      "id": "Zoo", 
      "label": "Zoo", 
      "properties": [
        "additionalType", 
        "description", 
        "image", 
        "name", 
        "url", 
        "address", 
        "aggregateRating", 
        "containedIn", 
        "event", 
        "events", 
        "faxNumber", 
        "geo", 
        "globalLocationNumber", 
        "interactionCount", 
        "isicV4", 
        "logo", 
        "map", 
        "maps", 
        "openingHoursSpecification", 
        "photo", 
        "photos", 
        "review", 
        "reviews", 
        "telephone", 
        "openingHours"
      ], 
      "specific_properties": [], 
      "subtypes": [], 
      "supertypes": [
        "CivicStructure"
      ], 
      "url": "http://schema.org/Zoo"
    }
  }, 
  "valid": "2013-06-23"
}
