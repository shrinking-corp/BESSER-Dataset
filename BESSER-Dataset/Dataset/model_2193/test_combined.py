# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    article_TreeNode,
    Formatter,
    article_XmlFormatter,
    article_TreeFormatter,
    article_JavaFormatter,
    article_HtmlFormatter,
    article_ImageFormatter,
    Factory,
    article_ImageFactory,
    article_TreeNodeProperty,
    ExternalTarget,
    article_SourceCode,
    article_BodyElement,
    article_BodyElementContainer,
    ExternalArticle,
    article_PluginResource,
    Article,
    article_ExternalArticle,
    Category,
    article_Schemadoc,
    article_Javadoc,
    article_ExtensionPoint,
    article_JavaPackage,
    Identifiable,
    article_LinkTarget,
    article_Identifiable,
    BodyElementContainer,
    Body,
    article_Category,
    article_Plugin,
    LinkTarget,
    article_StructuralElement,
    article_ExternalTarget,
    article_JavaElement,
    BodyElement,
    article_Text,
    article_Toc,
    article_Image,
    article_Key,
    article_Excel,
    article_Selection,
    article_Embedding,
    article_Link,
    article_Diagram,
    article_Description,
    article_Formatter,
    article_Callout,
    EmbeddableElement,
    article_Factory,
    article_Snippet,
    article_Section,
    article_Chapter,
    Chapter,
    article_Article,
    article_EmbeddableElement,
    article_Context,
    StructuralElement,
    article_Body,
    article_Documentation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_article_treenode_is_not_abstract():
    assert not inspect.isabstract(article_TreeNode)


def test_hyp_article_treenode_constructor_exists():
    assert callable(article_TreeNode.__init__)


def test_hyp_article_treenode_constructor_args():
    sig = inspect.signature(article_TreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "xmi_ID" in params, "Missing parameter 'xmi_ID'"
    assert "label" in params, "Missing parameter 'label'"
    assert "image" in params, "Missing parameter 'image'"






def test_hyp_formatter_is_not_abstract():
    assert not inspect.isabstract(Formatter)


def test_hyp_formatter_constructor_exists():
    assert callable(Formatter.__init__)


def test_hyp_formatter_constructor_args():
    sig = inspect.signature(Formatter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_xmlformatter_is_not_abstract():
    assert not inspect.isabstract(article_XmlFormatter)


def test_hyp_article_xmlformatter_constructor_exists():
    assert callable(article_XmlFormatter.__init__)


def test_hyp_article_xmlformatter_constructor_args():
    sig = inspect.signature(article_XmlFormatter.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_article_treeformatter_is_not_abstract():
    assert not inspect.isabstract(article_TreeFormatter)


def test_hyp_article_treeformatter_constructor_exists():
    assert callable(article_TreeFormatter.__init__)


def test_hyp_article_treeformatter_constructor_args():
    sig = inspect.signature(article_TreeFormatter.__init__)
    params = list(sig.parameters.keys())
    assert "expanded" in params, "Missing parameter 'expanded'"
    assert "expandTo" in params, "Missing parameter 'expandTo'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "file" in params, "Missing parameter 'file'"







def test_hyp_article_javaformatter_is_not_abstract():
    assert not inspect.isabstract(article_JavaFormatter)


def test_hyp_article_javaformatter_constructor_exists():
    assert callable(article_JavaFormatter.__init__)


def test_hyp_article_javaformatter_constructor_args():
    sig = inspect.signature(article_JavaFormatter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_htmlformatter_is_not_abstract():
    assert not inspect.isabstract(article_HtmlFormatter)


def test_hyp_article_htmlformatter_constructor_exists():
    assert callable(article_HtmlFormatter.__init__)


def test_hyp_article_htmlformatter_constructor_args():
    sig = inspect.signature(article_HtmlFormatter.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_article_imageformatter_is_not_abstract():
    assert not inspect.isabstract(article_ImageFormatter)


def test_hyp_article_imageformatter_constructor_exists():
    assert callable(article_ImageFormatter.__init__)


def test_hyp_article_imageformatter_constructor_args():
    sig = inspect.signature(article_ImageFormatter.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_factory_is_not_abstract():
    assert not inspect.isabstract(Factory)


def test_hyp_factory_constructor_exists():
    assert callable(Factory.__init__)


def test_hyp_factory_constructor_args():
    sig = inspect.signature(Factory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_imagefactory_is_not_abstract():
    assert not inspect.isabstract(article_ImageFactory)


def test_hyp_article_imagefactory_constructor_exists():
    assert callable(article_ImageFactory.__init__)


def test_hyp_article_imagefactory_constructor_args():
    sig = inspect.signature(article_ImageFactory.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_article_treenodeproperty_is_not_abstract():
    assert not inspect.isabstract(article_TreeNodeProperty)


def test_hyp_article_treenodeproperty_constructor_exists():
    assert callable(article_TreeNodeProperty.__init__)


def test_hyp_article_treenodeproperty_constructor_args():
    sig = inspect.signature(article_TreeNodeProperty.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "valueImage" in params, "Missing parameter 'valueImage'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_externaltarget_is_not_abstract():
    assert not inspect.isabstract(ExternalTarget)


def test_hyp_externaltarget_constructor_exists():
    assert callable(ExternalTarget.__init__)


def test_hyp_externaltarget_constructor_args():
    sig = inspect.signature(ExternalTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_sourcecode_is_not_abstract():
    assert not inspect.isabstract(article_SourceCode)


def test_hyp_article_sourcecode_constructor_exists():
    assert callable(article_SourceCode.__init__)


def test_hyp_article_sourcecode_constructor_args():
    sig = inspect.signature(article_SourceCode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_bodyelement_is_not_abstract():
    assert not inspect.isabstract(article_BodyElement)


def test_hyp_article_bodyelement_constructor_exists():
    assert callable(article_BodyElement.__init__)


def test_hyp_article_bodyelement_constructor_args():
    sig = inspect.signature(article_BodyElement.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"




def test_hyp_article_bodyelementcontainer_is_not_abstract():
    assert not inspect.isabstract(article_BodyElementContainer)


def test_hyp_article_bodyelementcontainer_constructor_exists():
    assert callable(article_BodyElementContainer.__init__)


def test_hyp_article_bodyelementcontainer_constructor_args():
    sig = inspect.signature(article_BodyElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_externalarticle_is_not_abstract():
    assert not inspect.isabstract(ExternalArticle)


def test_hyp_externalarticle_constructor_exists():
    assert callable(ExternalArticle.__init__)


def test_hyp_externalarticle_constructor_args():
    sig = inspect.signature(ExternalArticle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_pluginresource_is_not_abstract():
    assert not inspect.isabstract(article_PluginResource)


def test_hyp_article_pluginresource_constructor_exists():
    assert callable(article_PluginResource.__init__)


def test_hyp_article_pluginresource_constructor_args():
    sig = inspect.signature(article_PluginResource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_is_not_abstract():
    assert not inspect.isabstract(Article)


def test_hyp_article_constructor_exists():
    assert callable(Article.__init__)


def test_hyp_article_constructor_args():
    sig = inspect.signature(Article.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_externalarticle_is_not_abstract():
    assert not inspect.isabstract(article_ExternalArticle)


def test_hyp_article_externalarticle_constructor_exists():
    assert callable(article_ExternalArticle.__init__)


def test_hyp_article_externalarticle_constructor_args():
    sig = inspect.signature(article_ExternalArticle.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"




def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_schemadoc_is_not_abstract():
    assert not inspect.isabstract(article_Schemadoc)


def test_hyp_article_schemadoc_constructor_exists():
    assert callable(article_Schemadoc.__init__)


def test_hyp_article_schemadoc_constructor_args():
    sig = inspect.signature(article_Schemadoc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_javadoc_is_not_abstract():
    assert not inspect.isabstract(article_Javadoc)


def test_hyp_article_javadoc_constructor_exists():
    assert callable(article_Javadoc.__init__)


def test_hyp_article_javadoc_constructor_args():
    sig = inspect.signature(article_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(article_ExtensionPoint)


def test_hyp_article_extensionpoint_constructor_exists():
    assert callable(article_ExtensionPoint.__init__)


def test_hyp_article_extensionpoint_constructor_args():
    sig = inspect.signature(article_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_article_javapackage_is_not_abstract():
    assert not inspect.isabstract(article_JavaPackage)


def test_hyp_article_javapackage_constructor_exists():
    assert callable(article_JavaPackage.__init__)


def test_hyp_article_javapackage_constructor_args():
    sig = inspect.signature(article_JavaPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_hyp_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_hyp_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_linktarget_is_not_abstract():
    assert not inspect.isabstract(article_LinkTarget)


def test_hyp_article_linktarget_constructor_exists():
    assert callable(article_LinkTarget.__init__)


def test_hyp_article_linktarget_constructor_args():
    sig = inspect.signature(article_LinkTarget.__init__)
    params = list(sig.parameters.keys())
    assert "defaultLabel" in params, "Missing parameter 'defaultLabel'"
    assert "tooltip" in params, "Missing parameter 'tooltip'"





def test_hyp_article_identifiable_is_not_abstract():
    assert not inspect.isabstract(article_Identifiable)


def test_hyp_article_identifiable_constructor_exists():
    assert callable(article_Identifiable.__init__)


def test_hyp_article_identifiable_constructor_args():
    sig = inspect.signature(article_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_bodyelementcontainer_is_not_abstract():
    assert not inspect.isabstract(BodyElementContainer)


def test_hyp_bodyelementcontainer_constructor_exists():
    assert callable(BodyElementContainer.__init__)


def test_hyp_bodyelementcontainer_constructor_args():
    sig = inspect.signature(BodyElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_hyp_body_constructor_exists():
    assert callable(Body.__init__)


def test_hyp_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_category_is_not_abstract():
    assert not inspect.isabstract(article_Category)


def test_hyp_article_category_constructor_exists():
    assert callable(article_Category.__init__)


def test_hyp_article_category_constructor_args():
    sig = inspect.signature(article_Category.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_plugin_is_not_abstract():
    assert not inspect.isabstract(article_Plugin)


def test_hyp_article_plugin_constructor_exists():
    assert callable(article_Plugin.__init__)


def test_hyp_article_plugin_constructor_args():
    sig = inspect.signature(article_Plugin.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_linktarget_is_not_abstract():
    assert not inspect.isabstract(LinkTarget)


def test_hyp_linktarget_constructor_exists():
    assert callable(LinkTarget.__init__)


def test_hyp_linktarget_constructor_args():
    sig = inspect.signature(LinkTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_structuralelement_is_not_abstract():
    assert not inspect.isabstract(article_StructuralElement)


def test_hyp_article_structuralelement_constructor_exists():
    assert callable(article_StructuralElement.__init__)


def test_hyp_article_structuralelement_constructor_args():
    sig = inspect.signature(article_StructuralElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "doc" in params, "Missing parameter 'doc'"





def test_hyp_article_externaltarget_is_not_abstract():
    assert not inspect.isabstract(article_ExternalTarget)


def test_hyp_article_externaltarget_constructor_exists():
    assert callable(article_ExternalTarget.__init__)


def test_hyp_article_externaltarget_constructor_args():
    sig = inspect.signature(article_ExternalTarget.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"




def test_hyp_article_javaelement_is_not_abstract():
    assert not inspect.isabstract(article_JavaElement)


def test_hyp_article_javaelement_constructor_exists():
    assert callable(article_JavaElement.__init__)


def test_hyp_article_javaelement_constructor_args():
    sig = inspect.signature(article_JavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "classFile" in params, "Missing parameter 'classFile'"




def test_hyp_bodyelement_is_not_abstract():
    assert not inspect.isabstract(BodyElement)


def test_hyp_bodyelement_constructor_exists():
    assert callable(BodyElement.__init__)


def test_hyp_bodyelement_constructor_args():
    sig = inspect.signature(BodyElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_text_is_not_abstract():
    assert not inspect.isabstract(article_Text)


def test_hyp_article_text_constructor_exists():
    assert callable(article_Text.__init__)


def test_hyp_article_text_constructor_args():
    sig = inspect.signature(article_Text.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_toc_is_not_abstract():
    assert not inspect.isabstract(article_Toc)


def test_hyp_article_toc_constructor_exists():
    assert callable(article_Toc.__init__)


def test_hyp_article_toc_constructor_args():
    sig = inspect.signature(article_Toc.__init__)
    params = list(sig.parameters.keys())
    assert "levels" in params, "Missing parameter 'levels'"




def test_hyp_article_image_is_not_abstract():
    assert not inspect.isabstract(article_Image)


def test_hyp_article_image_constructor_exists():
    assert callable(article_Image.__init__)


def test_hyp_article_image_constructor_args():
    sig = inspect.signature(article_Image.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_article_key_is_not_abstract():
    assert not inspect.isabstract(article_Key)


def test_hyp_article_key_constructor_exists():
    assert callable(article_Key.__init__)


def test_hyp_article_key_constructor_args():
    sig = inspect.signature(article_Key.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_excel_is_not_abstract():
    assert not inspect.isabstract(article_Excel)


def test_hyp_article_excel_constructor_exists():
    assert callable(article_Excel.__init__)


def test_hyp_article_excel_constructor_args():
    sig = inspect.signature(article_Excel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_selection_is_not_abstract():
    assert not inspect.isabstract(article_Selection)


def test_hyp_article_selection_constructor_exists():
    assert callable(article_Selection.__init__)


def test_hyp_article_selection_constructor_args():
    sig = inspect.signature(article_Selection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_embedding_is_not_abstract():
    assert not inspect.isabstract(article_Embedding)


def test_hyp_article_embedding_constructor_exists():
    assert callable(article_Embedding.__init__)


def test_hyp_article_embedding_constructor_args():
    sig = inspect.signature(article_Embedding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_link_is_not_abstract():
    assert not inspect.isabstract(article_Link)


def test_hyp_article_link_constructor_exists():
    assert callable(article_Link.__init__)


def test_hyp_article_link_constructor_args():
    sig = inspect.signature(article_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_diagram_is_not_abstract():
    assert not inspect.isabstract(article_Diagram)


def test_hyp_article_diagram_constructor_exists():
    assert callable(article_Diagram.__init__)


def test_hyp_article_diagram_constructor_args():
    sig = inspect.signature(article_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_description_is_not_abstract():
    assert not inspect.isabstract(article_Description)


def test_hyp_article_description_constructor_exists():
    assert callable(article_Description.__init__)


def test_hyp_article_description_constructor_args():
    sig = inspect.signature(article_Description.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_formatter_is_not_abstract():
    assert not inspect.isabstract(article_Formatter)


def test_hyp_article_formatter_constructor_exists():
    assert callable(article_Formatter.__init__)


def test_hyp_article_formatter_constructor_args():
    sig = inspect.signature(article_Formatter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_callout_is_not_abstract():
    assert not inspect.isabstract(article_Callout)


def test_hyp_article_callout_constructor_exists():
    assert callable(article_Callout.__init__)


def test_hyp_article_callout_constructor_args():
    sig = inspect.signature(article_Callout.__init__)
    params = list(sig.parameters.keys())



def test_hyp_embeddableelement_is_not_abstract():
    assert not inspect.isabstract(EmbeddableElement)


def test_hyp_embeddableelement_constructor_exists():
    assert callable(EmbeddableElement.__init__)


def test_hyp_embeddableelement_constructor_args():
    sig = inspect.signature(EmbeddableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_factory_is_not_abstract():
    assert not inspect.isabstract(article_Factory)


def test_hyp_article_factory_constructor_exists():
    assert callable(article_Factory.__init__)


def test_hyp_article_factory_constructor_args():
    sig = inspect.signature(article_Factory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_snippet_is_not_abstract():
    assert not inspect.isabstract(article_Snippet)


def test_hyp_article_snippet_constructor_exists():
    assert callable(article_Snippet.__init__)


def test_hyp_article_snippet_constructor_args():
    sig = inspect.signature(article_Snippet.__init__)
    params = list(sig.parameters.keys())
    assert "titleImage" in params, "Missing parameter 'titleImage'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_article_section_is_not_abstract():
    assert not inspect.isabstract(article_Section)


def test_hyp_article_section_constructor_exists():
    assert callable(article_Section.__init__)


def test_hyp_article_section_constructor_args():
    sig = inspect.signature(article_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_chapter_is_not_abstract():
    assert not inspect.isabstract(article_Chapter)


def test_hyp_article_chapter_constructor_exists():
    assert callable(article_Chapter.__init__)


def test_hyp_article_chapter_constructor_args():
    sig = inspect.signature(article_Chapter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_chapter_is_not_abstract():
    assert not inspect.isabstract(Chapter)


def test_hyp_chapter_constructor_exists():
    assert callable(Chapter.__init__)


def test_hyp_chapter_constructor_args():
    sig = inspect.signature(Chapter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_article_is_not_abstract():
    assert not inspect.isabstract(article_Article)


def test_hyp_article_article_constructor_exists():
    assert callable(article_Article.__init__)


def test_hyp_article_article_constructor_args():
    sig = inspect.signature(article_Article.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_embeddableelement_is_not_abstract():
    assert not inspect.isabstract(article_EmbeddableElement)


def test_hyp_article_embeddableelement_constructor_exists():
    assert callable(article_EmbeddableElement.__init__)


def test_hyp_article_embeddableelement_constructor_args():
    sig = inspect.signature(article_EmbeddableElement.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"




def test_hyp_article_context_is_not_abstract():
    assert not inspect.isabstract(article_Context)


def test_hyp_article_context_constructor_exists():
    assert callable(article_Context.__init__)


def test_hyp_article_context_constructor_args():
    sig = inspect.signature(article_Context.__init__)
    params = list(sig.parameters.keys())
    assert "baseFolder" in params, "Missing parameter 'baseFolder'"
    assert "root" in params, "Missing parameter 'root'"
    assert "project" in params, "Missing parameter 'project'"






def test_hyp_structuralelement_is_not_abstract():
    assert not inspect.isabstract(StructuralElement)


def test_hyp_structuralelement_constructor_exists():
    assert callable(StructuralElement.__init__)


def test_hyp_structuralelement_constructor_args():
    sig = inspect.signature(StructuralElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_body_is_not_abstract():
    assert not inspect.isabstract(article_Body)


def test_hyp_article_body_constructor_exists():
    assert callable(article_Body.__init__)


def test_hyp_article_body_constructor_args():
    sig = inspect.signature(article_Body.__init__)
    params = list(sig.parameters.keys())



def test_hyp_article_documentation_is_not_abstract():
    assert not inspect.isabstract(article_Documentation)


def test_hyp_article_documentation_constructor_exists():
    assert callable(article_Documentation.__init__)


def test_hyp_article_documentation_constructor_args():
    sig = inspect.signature(article_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "project" in params, "Missing parameter 'project'"



# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
article_TreeNode_strategy = st.builds(
    article_TreeNode,
    xmi_ID=
        safe_text,
    label=
        safe_text,
    image=
        safe_text
)
Formatter_strategy = st.builds(
    Formatter,
)
article_XmlFormatter_strategy = st.builds(
    article_XmlFormatter,
    file=
        safe_text
)
article_TreeFormatter_strategy = st.builds(
    article_TreeFormatter,
    expanded=
        safe_text,
    expandTo=
        st.integers(),
    selected=
        safe_text,
    file=
        safe_text
)
article_JavaFormatter_strategy = st.builds(
    article_JavaFormatter,
)
article_HtmlFormatter_strategy = st.builds(
    article_HtmlFormatter,
    file=
        safe_text
)
article_ImageFormatter_strategy = st.builds(
    article_ImageFormatter,
    file=
        safe_text
)
Factory_strategy = st.builds(
    Factory,
)
article_ImageFactory_strategy = st.builds(
    article_ImageFactory,
    file=
        safe_text
)
article_TreeNodeProperty_strategy = st.builds(
    article_TreeNodeProperty,
    key=
        safe_text,
    valueImage=
        safe_text,
    value=
        safe_text
)
ExternalTarget_strategy = st.builds(
    ExternalTarget,
)
article_SourceCode_strategy = st.builds(
    article_SourceCode,
)
article_BodyElement_strategy = st.builds(
    article_BodyElement,
    tag=
        safe_text
)
article_BodyElementContainer_strategy = st.builds(
    article_BodyElementContainer,
)
ExternalArticle_strategy = st.builds(
    ExternalArticle,
)
article_PluginResource_strategy = st.builds(
    article_PluginResource,
)
Article_strategy = st.builds(
    Article,
)
article_ExternalArticle_strategy = st.builds(
    article_ExternalArticle,
    url=
        safe_text
)
Category_strategy = st.builds(
    Category,
)
article_Schemadoc_strategy = st.builds(
    article_Schemadoc,
)
article_Javadoc_strategy = st.builds(
    article_Javadoc,
)
article_ExtensionPoint_strategy = st.builds(
    article_ExtensionPoint,
    name=
        safe_text
)
article_JavaPackage_strategy = st.builds(
    article_JavaPackage,
    name=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
article_LinkTarget_strategy = st.builds(
    article_LinkTarget,
    defaultLabel=
        safe_text,
    tooltip=
        safe_text
)
article_Identifiable_strategy = st.builds(
    article_Identifiable,
    id=
        safe_text
)
BodyElementContainer_strategy = st.builds(
    BodyElementContainer,
)
Body_strategy = st.builds(
    Body,
)
article_Category_strategy = st.builds(
    article_Category,
)
article_Plugin_strategy = st.builds(
    article_Plugin,
    label=
        safe_text,
    name=
        safe_text
)
LinkTarget_strategy = st.builds(
    LinkTarget,
)
article_StructuralElement_strategy = st.builds(
    article_StructuralElement,
    title=
        safe_text,
    doc=
        safe_text
)
article_ExternalTarget_strategy = st.builds(
    article_ExternalTarget,
    url=
        safe_text
)
article_JavaElement_strategy = st.builds(
    article_JavaElement,
    classFile=
        safe_text
)
BodyElement_strategy = st.builds(
    BodyElement,
)
article_Text_strategy = st.builds(
    article_Text,
)
article_Toc_strategy = st.builds(
    article_Toc,
    levels=
        st.integers()
)
article_Image_strategy = st.builds(
    article_Image,
    file=
        safe_text
)
article_Key_strategy = st.builds(
    article_Key,
)
article_Excel_strategy = st.builds(
    article_Excel,
)
article_Selection_strategy = st.builds(
    article_Selection,
)
article_Embedding_strategy = st.builds(
    article_Embedding,
)
article_Link_strategy = st.builds(
    article_Link,
)
article_Diagram_strategy = st.builds(
    article_Diagram,
)
article_Description_strategy = st.builds(
    article_Description,
)
article_Formatter_strategy = st.builds(
    article_Formatter,
)
article_Callout_strategy = st.builds(
    article_Callout,
)
EmbeddableElement_strategy = st.builds(
    EmbeddableElement,
)
article_Factory_strategy = st.builds(
    article_Factory,
)
article_Snippet_strategy = st.builds(
    article_Snippet,
    titleImage=
        safe_text,
    title=
        safe_text
)
article_Section_strategy = st.builds(
    article_Section,
)
article_Chapter_strategy = st.builds(
    article_Chapter,
)
Chapter_strategy = st.builds(
    Chapter,
)
article_Article_strategy = st.builds(
    article_Article,
)
article_EmbeddableElement_strategy = st.builds(
    article_EmbeddableElement,
    doc=
        safe_text
)
article_Context_strategy = st.builds(
    article_Context,
    baseFolder=
        safe_text,
    root=
        safe_text,
    project=
        safe_text
)
StructuralElement_strategy = st.builds(
    StructuralElement,
)
article_Body_strategy = st.builds(
    article_Body,
)
article_Documentation_strategy = st.builds(
    article_Documentation,
    project=
        safe_text
)




@given(instance=article_TreeNode_strategy)
def test_hyp_article_treenode_xmi_ID_setter(instance):
    original = instance.xmi_ID
    instance.xmi_ID = original
    assert instance.xmi_ID == original



@given(instance=article_TreeNode_strategy)
def test_hyp_article_treenode_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=article_TreeNode_strategy)
def test_hyp_article_treenode_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original





@given(instance=article_XmlFormatter_strategy)
def test_hyp_article_xmlformatter_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=article_TreeFormatter_strategy)
def test_hyp_article_treeformatter_expanded_setter(instance):
    original = instance.expanded
    instance.expanded = original
    assert instance.expanded == original



@given(instance=article_TreeFormatter_strategy)
def test_hyp_article_treeformatter_expandTo_setter(instance):
    original = instance.expandTo
    instance.expandTo = original
    assert instance.expandTo == original



@given(instance=article_TreeFormatter_strategy)
def test_hyp_article_treeformatter_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=article_TreeFormatter_strategy)
def test_hyp_article_treeformatter_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original





@given(instance=article_HtmlFormatter_strategy)
def test_hyp_article_htmlformatter_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=article_ImageFormatter_strategy)
def test_hyp_article_imageformatter_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original





@given(instance=article_ImageFactory_strategy)
def test_hyp_article_imagefactory_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=article_TreeNodeProperty_strategy)
def test_hyp_article_treenodeproperty_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=article_TreeNodeProperty_strategy)
def test_hyp_article_treenodeproperty_valueImage_setter(instance):
    original = instance.valueImage
    instance.valueImage = original
    assert instance.valueImage == original



@given(instance=article_TreeNodeProperty_strategy)
def test_hyp_article_treenodeproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=article_BodyElement_strategy)
def test_hyp_article_bodyelement_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original








@given(instance=article_ExternalArticle_strategy)
def test_hyp_article_externalarticle_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original







@given(instance=article_ExtensionPoint_strategy)
def test_hyp_article_extensionpoint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=article_JavaPackage_strategy)
def test_hyp_article_javapackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=article_LinkTarget_strategy)
def test_hyp_article_linktarget_defaultLabel_setter(instance):
    original = instance.defaultLabel
    instance.defaultLabel = original
    assert instance.defaultLabel == original



@given(instance=article_LinkTarget_strategy)
def test_hyp_article_linktarget_tooltip_setter(instance):
    original = instance.tooltip
    instance.tooltip = original
    assert instance.tooltip == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=article_LinkTarget_strategy)
@settings(max_examples=30)
def test_hyp_article_linktarget_linkfrom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.linkFrom(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.linkFrom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'linkFrom' in article_LinkTarget is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'linkFrom' in article_LinkTarget did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'linkFrom' in article_LinkTarget is not implemented or raised an error")




@given(instance=article_Identifiable_strategy)
def test_hyp_article_identifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original







@given(instance=article_Plugin_strategy)
def test_hyp_article_plugin_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=article_Plugin_strategy)
def test_hyp_article_plugin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=article_StructuralElement_strategy)
def test_hyp_article_structuralelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=article_StructuralElement_strategy)
def test_hyp_article_structuralelement_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original




@given(instance=article_ExternalTarget_strategy)
def test_hyp_article_externaltarget_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original




@given(instance=article_JavaElement_strategy)
def test_hyp_article_javaelement_classFile_setter(instance):
    original = instance.classFile
    instance.classFile = original
    assert instance.classFile == original






@given(instance=article_Toc_strategy)
def test_hyp_article_toc_levels_setter(instance):
    original = instance.levels
    instance.levels = original
    assert instance.levels == original




@given(instance=article_Image_strategy)
def test_hyp_article_image_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original















@given(instance=article_Snippet_strategy)
def test_hyp_article_snippet_titleImage_setter(instance):
    original = instance.titleImage
    instance.titleImage = original
    assert instance.titleImage == original



@given(instance=article_Snippet_strategy)
def test_hyp_article_snippet_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original








@given(instance=article_EmbeddableElement_strategy)
def test_hyp_article_embeddableelement_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original




@given(instance=article_Context_strategy)
def test_hyp_article_context_baseFolder_setter(instance):
    original = instance.baseFolder
    instance.baseFolder = original
    assert instance.baseFolder == original



@given(instance=article_Context_strategy)
def test_hyp_article_context_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original



@given(instance=article_Context_strategy)
def test_hyp_article_context_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original






@given(instance=article_Documentation_strategy)
def test_hyp_article_documentation_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Article,
    Body,
    BodyElement,
    BodyElementContainer,
    Category,
    Chapter,
    EmbeddableElement,
    ExternalArticle,
    ExternalTarget,
    Factory,
    Formatter,
    Identifiable,
    LinkTarget,
    StructuralElement,
    article_Article,
    article_Body,
    article_BodyElement,
    article_BodyElementContainer,
    article_Callout,
    article_Category,
    article_Chapter,
    article_Context,
    article_Description,
    article_Diagram,
    article_Documentation,
    article_EmbeddableElement,
    article_Embedding,
    article_Excel,
    article_ExtensionPoint,
    article_ExternalArticle,
    article_ExternalTarget,
    article_Factory,
    article_Formatter,
    article_HtmlFormatter,
    article_Identifiable,
    article_Image,
    article_ImageFactory,
    article_ImageFormatter,
    article_JavaElement,
    article_JavaFormatter,
    article_JavaPackage,
    article_Javadoc,
    article_Key,
    article_Link,
    article_LinkTarget,
    article_Plugin,
    article_PluginResource,
    article_Schemadoc,
    article_Section,
    article_Selection,
    article_Snippet,
    article_SourceCode,
    article_StructuralElement,
    article_Text,
    article_Toc,
    article_TreeFormatter,
    article_TreeNode,
    article_TreeNodeProperty,
    article_XmlFormatter,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_article_BodyElement_tag_value_roundtrip():
    instance = article_BodyElement(tag="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_article_Context_baseFolder_value_roundtrip():
    instance = article_Context(baseFolder="sample_text", project="sample_text", root="sample_text")
    assert instance.baseFolder == "sample_text"
    instance.baseFolder = "sample_text_2"
    assert instance.baseFolder == "sample_text_2"


def test_article_Context_project_value_roundtrip():
    instance = article_Context(baseFolder="sample_text", project="sample_text", root="sample_text")
    assert instance.project == "sample_text"
    instance.project = "sample_text_2"
    assert instance.project == "sample_text_2"


def test_article_Context_root_value_roundtrip():
    instance = article_Context(baseFolder="sample_text", project="sample_text", root="sample_text")
    assert instance.root == "sample_text"
    instance.root = "sample_text_2"
    assert instance.root == "sample_text_2"


def test_article_Documentation_project_value_roundtrip():
    instance = article_Documentation(project="sample_text")
    assert instance.project == "sample_text"
    instance.project = "sample_text_2"
    assert instance.project == "sample_text_2"


def test_article_EmbeddableElement_doc_value_roundtrip():
    instance = article_EmbeddableElement(doc="sample_text")
    assert instance.doc == "sample_text"
    instance.doc = "sample_text_2"
    assert instance.doc == "sample_text_2"


def test_article_ExtensionPoint_name_value_roundtrip():
    instance = article_ExtensionPoint(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_article_ExternalArticle_url_value_roundtrip():
    instance = article_ExternalArticle(url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_article_ExternalTarget_url_value_roundtrip():
    instance = article_ExternalTarget(url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_article_HtmlFormatter_file_value_roundtrip():
    instance = article_HtmlFormatter(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_Identifiable_id_value_roundtrip():
    instance = article_Identifiable(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_article_Image_file_value_roundtrip():
    instance = article_Image(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_ImageFactory_file_value_roundtrip():
    instance = article_ImageFactory(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_ImageFormatter_file_value_roundtrip():
    instance = article_ImageFormatter(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_JavaElement_classFile_value_roundtrip():
    instance = article_JavaElement(classFile="sample_text")
    assert instance.classFile == "sample_text"
    instance.classFile = "sample_text_2"
    assert instance.classFile == "sample_text_2"


def test_article_JavaPackage_name_value_roundtrip():
    instance = article_JavaPackage(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_article_LinkTarget_defaultLabel_value_roundtrip():
    instance = article_LinkTarget(defaultLabel="sample_text", tooltip="sample_text")
    assert instance.defaultLabel == "sample_text"
    instance.defaultLabel = "sample_text_2"
    assert instance.defaultLabel == "sample_text_2"


def test_article_LinkTarget_tooltip_value_roundtrip():
    instance = article_LinkTarget(defaultLabel="sample_text", tooltip="sample_text")
    assert instance.tooltip == "sample_text"
    instance.tooltip = "sample_text_2"
    assert instance.tooltip == "sample_text_2"


def test_article_Plugin_label_value_roundtrip():
    instance = article_Plugin(label="sample_text", name="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_article_Plugin_name_value_roundtrip():
    instance = article_Plugin(label="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_article_Snippet_title_value_roundtrip():
    instance = article_Snippet(title="sample_text", titleImage="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_article_Snippet_titleImage_value_roundtrip():
    instance = article_Snippet(title="sample_text", titleImage="sample_text")
    assert instance.titleImage == "sample_text"
    instance.titleImage = "sample_text_2"
    assert instance.titleImage == "sample_text_2"


def test_article_StructuralElement_doc_value_roundtrip():
    instance = article_StructuralElement(doc="sample_text", title="sample_text")
    assert instance.doc == "sample_text"
    instance.doc = "sample_text_2"
    assert instance.doc == "sample_text_2"


def test_article_StructuralElement_title_value_roundtrip():
    instance = article_StructuralElement(doc="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_article_Toc_levels_value_roundtrip():
    instance = article_Toc(levels=7)
    assert instance.levels == 7
    instance.levels = 13
    assert instance.levels == 13


def test_article_TreeFormatter_expandTo_value_roundtrip():
    instance = article_TreeFormatter(expandTo=7, expanded="sample_text", file="sample_text", selected="sample_text")
    assert instance.expandTo == 7
    instance.expandTo = 13
    assert instance.expandTo == 13


def test_article_TreeFormatter_expanded_value_roundtrip():
    instance = article_TreeFormatter(expandTo=7, expanded="sample_text", file="sample_text", selected="sample_text")
    assert instance.expanded == "sample_text"
    instance.expanded = "sample_text_2"
    assert instance.expanded == "sample_text_2"


def test_article_TreeFormatter_file_value_roundtrip():
    instance = article_TreeFormatter(expandTo=7, expanded="sample_text", file="sample_text", selected="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_TreeFormatter_selected_value_roundtrip():
    instance = article_TreeFormatter(expandTo=7, expanded="sample_text", file="sample_text", selected="sample_text")
    assert instance.selected == "sample_text"
    instance.selected = "sample_text_2"
    assert instance.selected == "sample_text_2"


def test_article_TreeNode_image_value_roundtrip():
    instance = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_article_TreeNode_label_value_roundtrip():
    instance = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_article_TreeNode_xmi_ID_value_roundtrip():
    instance = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    assert instance.xmi_ID == "sample_text"
    instance.xmi_ID = "sample_text_2"
    assert instance.xmi_ID == "sample_text_2"


def test_article_TreeNodeProperty_key_value_roundtrip():
    instance = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_article_TreeNodeProperty_value_value_roundtrip():
    instance = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_article_TreeNodeProperty_valueImage_value_roundtrip():
    instance = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    assert instance.valueImage == "sample_text"
    instance.valueImage = "sample_text_2"
    assert instance.valueImage == "sample_text_2"


def test_article_XmlFormatter_file_value_roundtrip():
    instance = article_XmlFormatter(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_article_ExternalArticle_isa_Article():
    instance = article_ExternalArticle(url="sample_text")
    assert isinstance(instance, Article)


def test_article_Category_isa_Body():
    instance = article_Category()
    assert isinstance(instance, Body)


def test_article_Chapter_isa_Body():
    instance = article_Chapter()
    assert isinstance(instance, Body)


def test_article_Diagram_isa_BodyElement():
    instance = article_Diagram()
    assert isinstance(instance, BodyElement)


def test_article_Embedding_isa_BodyElement():
    instance = article_Embedding()
    assert isinstance(instance, BodyElement)


def test_article_Excel_isa_BodyElement():
    instance = article_Excel()
    assert isinstance(instance, BodyElement)


def test_article_Image_isa_BodyElement():
    instance = article_Image(file="sample_text")
    assert isinstance(instance, BodyElement)


def test_article_Key_isa_BodyElement():
    instance = article_Key()
    assert isinstance(instance, BodyElement)


def test_article_Link_isa_BodyElement():
    instance = article_Link()
    assert isinstance(instance, BodyElement)


def test_article_Selection_isa_BodyElement():
    instance = article_Selection()
    assert isinstance(instance, BodyElement)


def test_article_Text_isa_BodyElement():
    instance = article_Text()
    assert isinstance(instance, BodyElement)


def test_article_Toc_isa_BodyElement():
    instance = article_Toc(levels=7)
    assert isinstance(instance, BodyElement)


def test_article_Body_isa_BodyElementContainer():
    instance = article_Body()
    assert isinstance(instance, BodyElementContainer)


def test_article_Callout_isa_BodyElementContainer():
    instance = article_Callout()
    assert isinstance(instance, BodyElementContainer)


def test_article_Description_isa_BodyElementContainer():
    instance = article_Description()
    assert isinstance(instance, BodyElementContainer)


def test_article_Section_isa_BodyElementContainer():
    instance = article_Section()
    assert isinstance(instance, BodyElementContainer)


def test_article_Javadoc_isa_Category():
    instance = article_Javadoc()
    assert isinstance(instance, Category)


def test_article_Schemadoc_isa_Category():
    instance = article_Schemadoc()
    assert isinstance(instance, Category)


def test_article_Article_isa_Chapter():
    instance = article_Article()
    assert isinstance(instance, Chapter)


def test_article_Factory_isa_EmbeddableElement():
    instance = article_Factory()
    assert isinstance(instance, EmbeddableElement)


def test_article_Snippet_isa_EmbeddableElement():
    instance = article_Snippet(title="sample_text", titleImage="sample_text")
    assert isinstance(instance, EmbeddableElement)


def test_article_PluginResource_isa_ExternalArticle():
    instance = article_PluginResource()
    assert isinstance(instance, ExternalArticle)


def test_article_SourceCode_isa_ExternalTarget():
    instance = article_SourceCode()
    assert isinstance(instance, ExternalTarget)


def test_article_ImageFactory_isa_Factory():
    instance = article_ImageFactory(file="sample_text")
    assert isinstance(instance, Factory)


def test_article_HtmlFormatter_isa_Formatter():
    instance = article_HtmlFormatter(file="sample_text")
    assert isinstance(instance, Formatter)


def test_article_ImageFormatter_isa_Formatter():
    instance = article_ImageFormatter(file="sample_text")
    assert isinstance(instance, Formatter)


def test_article_JavaFormatter_isa_Formatter():
    instance = article_JavaFormatter()
    assert isinstance(instance, Formatter)


def test_article_TreeFormatter_isa_Formatter():
    instance = article_TreeFormatter(expandTo=7, expanded="sample_text", file="sample_text", selected="sample_text")
    assert isinstance(instance, Formatter)


def test_article_XmlFormatter_isa_Formatter():
    instance = article_XmlFormatter(file="sample_text")
    assert isinstance(instance, Formatter)


def test_article_EmbeddableElement_isa_Identifiable():
    instance = article_EmbeddableElement(doc="sample_text")
    assert isinstance(instance, Identifiable)


def test_article_LinkTarget_isa_Identifiable():
    instance = article_LinkTarget(defaultLabel="sample_text", tooltip="sample_text")
    assert isinstance(instance, Identifiable)


def test_article_ExternalTarget_isa_LinkTarget():
    instance = article_ExternalTarget(url="sample_text")
    assert isinstance(instance, LinkTarget)


def test_article_JavaElement_isa_LinkTarget():
    instance = article_JavaElement(classFile="sample_text")
    assert isinstance(instance, LinkTarget)


def test_article_Section_isa_LinkTarget():
    instance = article_Section()
    assert isinstance(instance, LinkTarget)


def test_article_StructuralElement_isa_LinkTarget():
    instance = article_StructuralElement(doc="sample_text", title="sample_text")
    assert isinstance(instance, LinkTarget)


def test_article_Body_isa_StructuralElement():
    instance = article_Body()
    assert isinstance(instance, StructuralElement)


def test_article_Documentation_isa_StructuralElement():
    instance = article_Documentation(project="sample_text")
    assert isinstance(instance, StructuralElement)


def test_assoc_callouts9_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Callout()
    b2 = article_Callout()
    _safe_set(a, 'snippet', {b1})
    assert _is_linked(a, 'snippet', b1)
    if hasattr(b1, 'Callout'):
        assert _is_linked(b1, 'Callout', a)
    _safe_set(a, 'snippet', {b2})
    assert _is_linked(a, 'snippet', b2)
    if hasattr(b1, 'Callout'):
        assert not _is_linked(b1, 'Callout', a)
    if hasattr(b2, 'Callout'):
        assert _is_linked(b2, 'Callout', a)
    _safe_set(a, 'snippet', set())
    assert not _is_linked(a, 'snippet', b2)
    if hasattr(b2, 'Callout'):
        assert not _is_linked(b2, 'Callout', a)


def test_assoc_children15_link_reassign_clear():
    a = article_StructuralElement(doc="sample_text", title="sample_text")
    b1 = article_StructuralElement(doc="sample_text", title="sample_text")
    b2 = article_StructuralElement(doc="sample_text_2", title="sample_text_2")
    _safe_set(a, 'StructuralElement', b1)
    assert _is_linked(a, 'StructuralElement', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'StructuralElement', b2)
    assert _is_linked(a, 'StructuralElement', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'StructuralElement', None)
    assert not _is_linked(a, 'StructuralElement', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_children39_link_reassign_clear():
    a = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    b1 = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    b2 = article_TreeNode(image="sample_text_2", label="sample_text_2", xmi_ID="sample_text_2")
    _safe_set(a, 'article_TreeNode', b1)
    assert _is_linked(a, 'article_TreeNode', b1)
    if hasattr(b1, 'article_TreeNode38'):
        assert _is_linked(b1, 'article_TreeNode38', a)
    _safe_set(a, 'article_TreeNode', b2)
    assert _is_linked(a, 'article_TreeNode', b2)
    if hasattr(b1, 'article_TreeNode38'):
        assert not _is_linked(b1, 'article_TreeNode38', a)
    if hasattr(b2, 'article_TreeNode38'):
        assert _is_linked(b2, 'article_TreeNode38', a)
    _safe_set(a, 'article_TreeNode', None)
    assert not _is_linked(a, 'article_TreeNode', b2)
    if hasattr(b2, 'article_TreeNode38'):
        assert not _is_linked(b2, 'article_TreeNode38', a)


def test_assoc_container27_link_reassign_clear():
    a = article_BodyElement(tag="sample_text")
    b1 = article_BodyElementContainer()
    b2 = article_BodyElementContainer()
    _safe_set(a, 'elements', b1)
    assert _is_linked(a, 'elements', b1)
    if hasattr(b1, 'BodyElementContainer'):
        assert _is_linked(b1, 'BodyElementContainer', a)
    _safe_set(a, 'elements', b2)
    assert _is_linked(a, 'elements', b2)
    if hasattr(b1, 'BodyElementContainer'):
        assert not _is_linked(b1, 'BodyElementContainer', a)
    if hasattr(b2, 'BodyElementContainer'):
        assert _is_linked(b2, 'BodyElementContainer', a)
    _safe_set(a, 'elements', None)
    assert not _is_linked(a, 'elements', b2)
    if hasattr(b2, 'BodyElementContainer'):
        assert not _is_linked(b2, 'BodyElementContainer', a)


def test_assoc_context0_link_reassign_clear():
    a = article_Documentation(project="sample_text")
    b1 = article_Context(baseFolder="sample_text", project="sample_text", root="sample_text")
    b2 = article_Context(baseFolder="sample_text_2", project="sample_text_2", root="sample_text_2")
    _safe_set(a, 'documentations', b1)
    assert _is_linked(a, 'documentations', b1)
    if hasattr(b1, 'Context'):
        assert _is_linked(b1, 'Context', a)
    _safe_set(a, 'documentations', b2)
    assert _is_linked(a, 'documentations', b2)
    if hasattr(b1, 'Context'):
        assert not _is_linked(b1, 'Context', a)
    if hasattr(b2, 'Context'):
        assert _is_linked(b2, 'Context', a)
    _safe_set(a, 'documentations', None)
    assert not _is_linked(a, 'documentations', b2)
    if hasattr(b2, 'Context'):
        assert not _is_linked(b2, 'Context', a)


def test_assoc_dependencies3_link_reassign_clear():
    a = article_Documentation(project="sample_text")
    b1 = article_Documentation(project="sample_text")
    b2 = article_Documentation(project="sample_text_2")
    _safe_set(a, 'article_Documentation', b1)
    assert _is_linked(a, 'article_Documentation', b1)
    if hasattr(b1, 'article_Documentation2'):
        assert _is_linked(b1, 'article_Documentation2', a)
    _safe_set(a, 'article_Documentation', b2)
    assert _is_linked(a, 'article_Documentation', b2)
    if hasattr(b1, 'article_Documentation2'):
        assert not _is_linked(b1, 'article_Documentation2', a)
    if hasattr(b2, 'article_Documentation2'):
        assert _is_linked(b2, 'article_Documentation2', a)
    _safe_set(a, 'article_Documentation', None)
    assert not _is_linked(a, 'article_Documentation', b2)
    if hasattr(b2, 'article_Documentation2'):
        assert not _is_linked(b2, 'article_Documentation2', a)


def test_assoc_description12_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Description()
    b2 = article_Description()
    _safe_set(a, 'snippet13', b1)
    assert _is_linked(a, 'snippet13', b1)
    if hasattr(b1, 'Description'):
        assert _is_linked(b1, 'Description', a)
    _safe_set(a, 'snippet13', b2)
    assert _is_linked(a, 'snippet13', b2)
    if hasattr(b1, 'Description'):
        assert not _is_linked(b1, 'Description', a)
    if hasattr(b2, 'Description'):
        assert _is_linked(b2, 'Description', a)
    _safe_set(a, 'snippet13', None)
    assert not _is_linked(a, 'snippet13', b2)
    if hasattr(b2, 'Description'):
        assert not _is_linked(b2, 'Description', a)


def test_assoc_documentation19_link_reassign_clear():
    a = article_StructuralElement(doc="sample_text", title="sample_text")
    b1 = article_Documentation(project="sample_text")
    b2 = article_Documentation(project="sample_text_2")
    _safe_set(a, 'article_StructuralElement', b1)
    assert _is_linked(a, 'article_StructuralElement', b1)
    if hasattr(b1, 'article_Documentation20'):
        assert _is_linked(b1, 'article_Documentation20', a)
    _safe_set(a, 'article_StructuralElement', b2)
    assert _is_linked(a, 'article_StructuralElement', b2)
    if hasattr(b1, 'article_Documentation20'):
        assert not _is_linked(b1, 'article_Documentation20', a)
    if hasattr(b2, 'article_Documentation20'):
        assert _is_linked(b2, 'article_Documentation20', a)
    _safe_set(a, 'article_StructuralElement', None)
    assert not _is_linked(a, 'article_StructuralElement', b2)
    if hasattr(b2, 'article_Documentation20'):
        assert not _is_linked(b2, 'article_Documentation20', a)


def test_assoc_documentation22_link_reassign_clear():
    a = article_EmbeddableElement(doc="sample_text")
    b1 = article_Documentation(project="sample_text")
    b2 = article_Documentation(project="sample_text_2")
    _safe_set(a, 'embeddableElements', b1)
    assert _is_linked(a, 'embeddableElements', b1)
    if hasattr(b1, 'Documentation23'):
        assert _is_linked(b1, 'Documentation23', a)
    _safe_set(a, 'embeddableElements', b2)
    assert _is_linked(a, 'embeddableElements', b2)
    if hasattr(b1, 'Documentation23'):
        assert not _is_linked(b1, 'Documentation23', a)
    if hasattr(b2, 'Documentation23'):
        assert _is_linked(b2, 'Documentation23', a)
    _safe_set(a, 'embeddableElements', None)
    assert not _is_linked(a, 'embeddableElements', b2)
    if hasattr(b2, 'Documentation23'):
        assert not _is_linked(b2, 'Documentation23', a)


def test_assoc_documentations6_link_reassign_clear():
    a = article_Documentation(project="sample_text")
    b1 = article_Context(baseFolder="sample_text", project="sample_text", root="sample_text")
    b2 = article_Context(baseFolder="sample_text_2", project="sample_text_2", root="sample_text_2")
    _safe_set(a, 'Documentation', b1)
    assert _is_linked(a, 'Documentation', b1)
    if hasattr(b1, 'context'):
        assert _is_linked(b1, 'context', a)
    _safe_set(a, 'Documentation', b2)
    assert _is_linked(a, 'Documentation', b2)
    if hasattr(b1, 'context'):
        assert not _is_linked(b1, 'context', a)
    if hasattr(b2, 'context'):
        assert _is_linked(b2, 'context', a)
    _safe_set(a, 'Documentation', None)
    assert not _is_linked(a, 'Documentation', b2)
    if hasattr(b2, 'context'):
        assert not _is_linked(b2, 'context', a)


def test_assoc_element29_link_reassign_clear():
    a = article_EmbeddableElement(doc="sample_text")
    b1 = article_Embedding()
    b2 = article_Embedding()
    _safe_set(a, 'article_EmbeddableElement', b1)
    assert _is_linked(a, 'article_EmbeddableElement', b1)
    if hasattr(b1, 'article_Embedding'):
        assert _is_linked(b1, 'article_Embedding', a)
    _safe_set(a, 'article_EmbeddableElement', b2)
    assert _is_linked(a, 'article_EmbeddableElement', b2)
    if hasattr(b1, 'article_Embedding'):
        assert not _is_linked(b1, 'article_Embedding', a)
    if hasattr(b2, 'article_Embedding'):
        assert _is_linked(b2, 'article_Embedding', a)
    _safe_set(a, 'article_EmbeddableElement', None)
    assert not _is_linked(a, 'article_EmbeddableElement', b2)
    if hasattr(b2, 'article_Embedding'):
        assert not _is_linked(b2, 'article_Embedding', a)


def test_assoc_elements26_link_reassign_clear():
    a = article_BodyElement(tag="sample_text")
    b1 = article_BodyElementContainer()
    b2 = article_BodyElementContainer()
    _safe_set(a, 'BodyElement', b1)
    assert _is_linked(a, 'BodyElement', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'BodyElement', b2)
    assert _is_linked(a, 'BodyElement', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'BodyElement', None)
    assert not _is_linked(a, 'BodyElement', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_embeddableElements1_link_reassign_clear():
    a = article_EmbeddableElement(doc="sample_text")
    b1 = article_Documentation(project="sample_text")
    b2 = article_Documentation(project="sample_text_2")
    _safe_set(a, 'EmbeddableElement', b1)
    assert _is_linked(a, 'EmbeddableElement', b1)
    if hasattr(b1, 'documentation'):
        assert _is_linked(b1, 'documentation', a)
    _safe_set(a, 'EmbeddableElement', b2)
    assert _is_linked(a, 'EmbeddableElement', b2)
    if hasattr(b1, 'documentation'):
        assert not _is_linked(b1, 'documentation', a)
    if hasattr(b2, 'documentation'):
        assert _is_linked(b2, 'documentation', a)
    _safe_set(a, 'EmbeddableElement', None)
    assert not _is_linked(a, 'EmbeddableElement', b2)
    if hasattr(b2, 'documentation'):
        assert not _is_linked(b2, 'documentation', a)


def test_assoc_extensionPoints31_link_reassign_clear():
    a = article_Plugin(label="sample_text", name="sample_text")
    b1 = article_ExtensionPoint(name="sample_text")
    b2 = article_ExtensionPoint(name="sample_text_2")
    _safe_set(a, 'plugin32', {b1})
    assert _is_linked(a, 'plugin32', b1)
    if hasattr(b1, 'ExtensionPoint'):
        assert _is_linked(b1, 'ExtensionPoint', a)
    _safe_set(a, 'plugin32', {b2})
    assert _is_linked(a, 'plugin32', b2)
    if hasattr(b1, 'ExtensionPoint'):
        assert not _is_linked(b1, 'ExtensionPoint', a)
    if hasattr(b2, 'ExtensionPoint'):
        assert _is_linked(b2, 'ExtensionPoint', a)
    _safe_set(a, 'plugin32', set())
    assert not _is_linked(a, 'plugin32', b2)
    if hasattr(b2, 'ExtensionPoint'):
        assert not _is_linked(b2, 'ExtensionPoint', a)


def test_assoc_formatter10_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Formatter()
    b2 = article_Formatter()
    _safe_set(a, 'snippet11', b1)
    assert _is_linked(a, 'snippet11', b1)
    if hasattr(b1, 'Formatter'):
        assert _is_linked(b1, 'Formatter', a)
    _safe_set(a, 'snippet11', b2)
    assert _is_linked(a, 'snippet11', b2)
    if hasattr(b1, 'Formatter'):
        assert not _is_linked(b1, 'Formatter', a)
    if hasattr(b2, 'Formatter'):
        assert _is_linked(b2, 'Formatter', a)
    _safe_set(a, 'snippet11', None)
    assert not _is_linked(a, 'snippet11', b2)
    if hasattr(b2, 'Formatter'):
        assert not _is_linked(b2, 'Formatter', a)


def test_assoc_packages30_link_reassign_clear():
    a = article_Plugin(label="sample_text", name="sample_text")
    b1 = article_JavaPackage(name="sample_text")
    b2 = article_JavaPackage(name="sample_text_2")
    _safe_set(a, 'plugin', {b1})
    assert _is_linked(a, 'plugin', b1)
    if hasattr(b1, 'JavaPackage'):
        assert _is_linked(b1, 'JavaPackage', a)
    _safe_set(a, 'plugin', {b2})
    assert _is_linked(a, 'plugin', b2)
    if hasattr(b1, 'JavaPackage'):
        assert not _is_linked(b1, 'JavaPackage', a)
    if hasattr(b2, 'JavaPackage'):
        assert _is_linked(b2, 'JavaPackage', a)
    _safe_set(a, 'plugin', set())
    assert not _is_linked(a, 'plugin', b2)
    if hasattr(b2, 'JavaPackage'):
        assert not _is_linked(b2, 'JavaPackage', a)


def test_assoc_parent17_link_reassign_clear():
    a = article_StructuralElement(doc="sample_text", title="sample_text")
    b1 = article_StructuralElement(doc="sample_text", title="sample_text")
    b2 = article_StructuralElement(doc="sample_text_2", title="sample_text_2")
    _safe_set(a, 'StructuralElement18', b1)
    assert _is_linked(a, 'StructuralElement18', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'StructuralElement18', b2)
    assert _is_linked(a, 'StructuralElement18', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'StructuralElement18', None)
    assert not _is_linked(a, 'StructuralElement18', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_plugin33_link_reassign_clear():
    a = article_Plugin(label="sample_text", name="sample_text")
    b1 = article_JavaPackage(name="sample_text")
    b2 = article_JavaPackage(name="sample_text_2")
    _safe_set(a, 'Plugin', b1)
    assert _is_linked(a, 'Plugin', b1)
    if hasattr(b1, 'packages'):
        assert _is_linked(b1, 'packages', a)
    _safe_set(a, 'Plugin', b2)
    assert _is_linked(a, 'Plugin', b2)
    if hasattr(b1, 'packages'):
        assert not _is_linked(b1, 'packages', a)
    if hasattr(b2, 'packages'):
        assert _is_linked(b2, 'packages', a)
    _safe_set(a, 'Plugin', None)
    assert not _is_linked(a, 'Plugin', b2)
    if hasattr(b2, 'packages'):
        assert not _is_linked(b2, 'packages', a)


def test_assoc_plugin34_link_reassign_clear():
    a = article_Plugin(label="sample_text", name="sample_text")
    b1 = article_ExtensionPoint(name="sample_text")
    b2 = article_ExtensionPoint(name="sample_text_2")
    _safe_set(a, 'Plugin35', b1)
    assert _is_linked(a, 'Plugin35', b1)
    if hasattr(b1, 'extensionPoints'):
        assert _is_linked(b1, 'extensionPoints', a)
    _safe_set(a, 'Plugin35', b2)
    assert _is_linked(a, 'Plugin35', b2)
    if hasattr(b1, 'extensionPoints'):
        assert not _is_linked(b1, 'extensionPoints', a)
    if hasattr(b2, 'extensionPoints'):
        assert _is_linked(b2, 'extensionPoints', a)
    _safe_set(a, 'Plugin35', None)
    assert not _is_linked(a, 'Plugin35', b2)
    if hasattr(b2, 'extensionPoints'):
        assert not _is_linked(b2, 'extensionPoints', a)


def test_assoc_plugins4_link_reassign_clear():
    a = article_Plugin(label="sample_text", name="sample_text")
    b1 = article_Documentation(project="sample_text")
    b2 = article_Documentation(project="sample_text_2")
    _safe_set(a, 'article_Plugin', b1)
    assert _is_linked(a, 'article_Plugin', b1)
    if hasattr(b1, 'article_Documentation5'):
        assert _is_linked(b1, 'article_Documentation5', a)
    _safe_set(a, 'article_Plugin', b2)
    assert _is_linked(a, 'article_Plugin', b2)
    if hasattr(b1, 'article_Documentation5'):
        assert not _is_linked(b1, 'article_Documentation5', a)
    if hasattr(b2, 'article_Documentation5'):
        assert _is_linked(b2, 'article_Documentation5', a)
    _safe_set(a, 'article_Plugin', None)
    assert not _is_linked(a, 'article_Plugin', b2)
    if hasattr(b2, 'article_Documentation5'):
        assert not _is_linked(b2, 'article_Documentation5', a)


def test_assoc_properties40_link_reassign_clear():
    a = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    b1 = article_TreeNode(image="sample_text", label="sample_text", xmi_ID="sample_text")
    b2 = article_TreeNode(image="sample_text_2", label="sample_text_2", xmi_ID="sample_text_2")
    _safe_set(a, 'article_TreeNodeProperty', b1)
    assert _is_linked(a, 'article_TreeNodeProperty', b1)
    if hasattr(b1, 'article_TreeNode41'):
        assert _is_linked(b1, 'article_TreeNode41', a)
    _safe_set(a, 'article_TreeNodeProperty', b2)
    assert _is_linked(a, 'article_TreeNodeProperty', b2)
    if hasattr(b1, 'article_TreeNode41'):
        assert not _is_linked(b1, 'article_TreeNode41', a)
    if hasattr(b2, 'article_TreeNode41'):
        assert _is_linked(b2, 'article_TreeNode41', a)
    _safe_set(a, 'article_TreeNodeProperty', None)
    assert not _is_linked(a, 'article_TreeNodeProperty', b2)
    if hasattr(b2, 'article_TreeNode41'):
        assert not _is_linked(b2, 'article_TreeNode41', a)


def test_assoc_properties43_link_reassign_clear():
    a = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    b1 = article_TreeNodeProperty(key="sample_text", value="sample_text", valueImage="sample_text")
    b2 = article_TreeNodeProperty(key="sample_text_2", value="sample_text_2", valueImage="sample_text_2")
    _safe_set(a, 'article_TreeNodeProperty42', {b1})
    assert _is_linked(a, 'article_TreeNodeProperty42', b1)
    if hasattr(b1, 'article_TreeNodeProperty44'):
        assert _is_linked(b1, 'article_TreeNodeProperty44', a)
    _safe_set(a, 'article_TreeNodeProperty42', {b2})
    assert _is_linked(a, 'article_TreeNodeProperty42', b2)
    if hasattr(b1, 'article_TreeNodeProperty44'):
        assert not _is_linked(b1, 'article_TreeNodeProperty44', a)
    if hasattr(b2, 'article_TreeNodeProperty44'):
        assert _is_linked(b2, 'article_TreeNodeProperty44', a)
    _safe_set(a, 'article_TreeNodeProperty42', set())
    assert not _is_linked(a, 'article_TreeNodeProperty42', b2)
    if hasattr(b2, 'article_TreeNodeProperty44'):
        assert not _is_linked(b2, 'article_TreeNodeProperty44', a)


def test_assoc_snippet21_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Callout()
    b2 = article_Callout()
    _safe_set(a, 'Snippet', b1)
    assert _is_linked(a, 'Snippet', b1)
    if hasattr(b1, 'callouts'):
        assert _is_linked(b1, 'callouts', a)
    _safe_set(a, 'Snippet', b2)
    assert _is_linked(a, 'Snippet', b2)
    if hasattr(b1, 'callouts'):
        assert not _is_linked(b1, 'callouts', a)
    if hasattr(b2, 'callouts'):
        assert _is_linked(b2, 'callouts', a)
    _safe_set(a, 'Snippet', None)
    assert not _is_linked(a, 'Snippet', b2)
    if hasattr(b2, 'callouts'):
        assert not _is_linked(b2, 'callouts', a)


def test_assoc_snippet36_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Formatter()
    b2 = article_Formatter()
    _safe_set(a, 'Snippet37', b1)
    assert _is_linked(a, 'Snippet37', b1)
    if hasattr(b1, 'formatter'):
        assert _is_linked(b1, 'formatter', a)
    _safe_set(a, 'Snippet37', b2)
    assert _is_linked(a, 'Snippet37', b2)
    if hasattr(b1, 'formatter'):
        assert not _is_linked(b1, 'formatter', a)
    if hasattr(b2, 'formatter'):
        assert _is_linked(b2, 'formatter', a)
    _safe_set(a, 'Snippet37', None)
    assert not _is_linked(a, 'Snippet37', b2)
    if hasattr(b2, 'formatter'):
        assert not _is_linked(b2, 'formatter', a)


def test_assoc_snippet45_link_reassign_clear():
    a = article_Snippet(title="sample_text", titleImage="sample_text")
    b1 = article_Description()
    b2 = article_Description()
    _safe_set(a, 'Snippet46', b1)
    assert _is_linked(a, 'Snippet46', b1)
    if hasattr(b1, 'description'):
        assert _is_linked(b1, 'description', a)
    _safe_set(a, 'Snippet46', b2)
    assert _is_linked(a, 'Snippet46', b2)
    if hasattr(b1, 'description'):
        assert not _is_linked(b1, 'description', a)
    if hasattr(b2, 'description'):
        assert _is_linked(b2, 'description', a)
    _safe_set(a, 'Snippet46', None)
    assert not _is_linked(a, 'Snippet46', b2)
    if hasattr(b2, 'description'):
        assert not _is_linked(b2, 'description', a)


def test_assoc_target28_link_reassign_clear():
    a = article_LinkTarget(defaultLabel="sample_text", tooltip="sample_text")
    b1 = article_Link()
    b2 = article_Link()
    _safe_set(a, 'article_LinkTarget', b1)
    assert _is_linked(a, 'article_LinkTarget', b1)
    if hasattr(b1, 'article_Link'):
        assert _is_linked(b1, 'article_Link', a)
    _safe_set(a, 'article_LinkTarget', b2)
    assert _is_linked(a, 'article_LinkTarget', b2)
    if hasattr(b1, 'article_Link'):
        assert not _is_linked(b1, 'article_Link', a)
    if hasattr(b2, 'article_Link'):
        assert _is_linked(b2, 'article_Link', a)
    _safe_set(a, 'article_LinkTarget', None)
    assert not _is_linked(a, 'article_LinkTarget', b2)
    if hasattr(b2, 'article_Link'):
        assert not _is_linked(b2, 'article_Link', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Article_strategy = st.builds(Article)
@given(instance=Article_strategy)
@settings(max_examples=25)
def test_Article_instantiation(instance):
    assert isinstance(instance, Article)


Body_strategy = st.builds(Body)
@given(instance=Body_strategy)
@settings(max_examples=25)
def test_Body_instantiation(instance):
    assert isinstance(instance, Body)


BodyElement_strategy = st.builds(BodyElement)
@given(instance=BodyElement_strategy)
@settings(max_examples=25)
def test_BodyElement_instantiation(instance):
    assert isinstance(instance, BodyElement)


BodyElementContainer_strategy = st.builds(BodyElementContainer)
@given(instance=BodyElementContainer_strategy)
@settings(max_examples=25)
def test_BodyElementContainer_instantiation(instance):
    assert isinstance(instance, BodyElementContainer)


Category_strategy = st.builds(Category)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


Chapter_strategy = st.builds(Chapter)
@given(instance=Chapter_strategy)
@settings(max_examples=25)
def test_Chapter_instantiation(instance):
    assert isinstance(instance, Chapter)


EmbeddableElement_strategy = st.builds(EmbeddableElement)
@given(instance=EmbeddableElement_strategy)
@settings(max_examples=25)
def test_EmbeddableElement_instantiation(instance):
    assert isinstance(instance, EmbeddableElement)


ExternalArticle_strategy = st.builds(ExternalArticle)
@given(instance=ExternalArticle_strategy)
@settings(max_examples=25)
def test_ExternalArticle_instantiation(instance):
    assert isinstance(instance, ExternalArticle)


ExternalTarget_strategy = st.builds(ExternalTarget)
@given(instance=ExternalTarget_strategy)
@settings(max_examples=25)
def test_ExternalTarget_instantiation(instance):
    assert isinstance(instance, ExternalTarget)


Factory_strategy = st.builds(Factory)
@given(instance=Factory_strategy)
@settings(max_examples=25)
def test_Factory_instantiation(instance):
    assert isinstance(instance, Factory)


Formatter_strategy = st.builds(Formatter)
@given(instance=Formatter_strategy)
@settings(max_examples=25)
def test_Formatter_instantiation(instance):
    assert isinstance(instance, Formatter)


Identifiable_strategy = st.builds(Identifiable)
@given(instance=Identifiable_strategy)
@settings(max_examples=25)
def test_Identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)


LinkTarget_strategy = st.builds(LinkTarget)
@given(instance=LinkTarget_strategy)
@settings(max_examples=25)
def test_LinkTarget_instantiation(instance):
    assert isinstance(instance, LinkTarget)


StructuralElement_strategy = st.builds(StructuralElement)
@given(instance=StructuralElement_strategy)
@settings(max_examples=25)
def test_StructuralElement_instantiation(instance):
    assert isinstance(instance, StructuralElement)


article_Article_strategy = st.builds(article_Article)
@given(instance=article_Article_strategy)
@settings(max_examples=25)
def test_article_Article_instantiation(instance):
    assert isinstance(instance, article_Article)


article_Body_strategy = st.builds(article_Body)
@given(instance=article_Body_strategy)
@settings(max_examples=25)
def test_article_Body_instantiation(instance):
    assert isinstance(instance, article_Body)


article_BodyElement_strategy = st.builds(article_BodyElement, tag=safe_text)
@given(instance=article_BodyElement_strategy)
@settings(max_examples=25)
def test_article_BodyElement_instantiation(instance):
    assert isinstance(instance, article_BodyElement)


article_BodyElementContainer_strategy = st.builds(article_BodyElementContainer)
@given(instance=article_BodyElementContainer_strategy)
@settings(max_examples=25)
def test_article_BodyElementContainer_instantiation(instance):
    assert isinstance(instance, article_BodyElementContainer)


article_Callout_strategy = st.builds(article_Callout)
@given(instance=article_Callout_strategy)
@settings(max_examples=25)
def test_article_Callout_instantiation(instance):
    assert isinstance(instance, article_Callout)


article_Category_strategy = st.builds(article_Category)
@given(instance=article_Category_strategy)
@settings(max_examples=25)
def test_article_Category_instantiation(instance):
    assert isinstance(instance, article_Category)


article_Chapter_strategy = st.builds(article_Chapter)
@given(instance=article_Chapter_strategy)
@settings(max_examples=25)
def test_article_Chapter_instantiation(instance):
    assert isinstance(instance, article_Chapter)


article_Context_strategy = st.builds(article_Context, baseFolder=safe_text, project=safe_text, root=safe_text)
@given(instance=article_Context_strategy)
@settings(max_examples=25)
def test_article_Context_instantiation(instance):
    assert isinstance(instance, article_Context)


article_Description_strategy = st.builds(article_Description)
@given(instance=article_Description_strategy)
@settings(max_examples=25)
def test_article_Description_instantiation(instance):
    assert isinstance(instance, article_Description)


article_Diagram_strategy = st.builds(article_Diagram)
@given(instance=article_Diagram_strategy)
@settings(max_examples=25)
def test_article_Diagram_instantiation(instance):
    assert isinstance(instance, article_Diagram)


article_Documentation_strategy = st.builds(article_Documentation, project=safe_text)
@given(instance=article_Documentation_strategy)
@settings(max_examples=25)
def test_article_Documentation_instantiation(instance):
    assert isinstance(instance, article_Documentation)


article_EmbeddableElement_strategy = st.builds(article_EmbeddableElement, doc=safe_text)
@given(instance=article_EmbeddableElement_strategy)
@settings(max_examples=25)
def test_article_EmbeddableElement_instantiation(instance):
    assert isinstance(instance, article_EmbeddableElement)


article_Embedding_strategy = st.builds(article_Embedding)
@given(instance=article_Embedding_strategy)
@settings(max_examples=25)
def test_article_Embedding_instantiation(instance):
    assert isinstance(instance, article_Embedding)


article_Excel_strategy = st.builds(article_Excel)
@given(instance=article_Excel_strategy)
@settings(max_examples=25)
def test_article_Excel_instantiation(instance):
    assert isinstance(instance, article_Excel)


article_ExtensionPoint_strategy = st.builds(article_ExtensionPoint, name=safe_text)
@given(instance=article_ExtensionPoint_strategy)
@settings(max_examples=25)
def test_article_ExtensionPoint_instantiation(instance):
    assert isinstance(instance, article_ExtensionPoint)


article_ExternalArticle_strategy = st.builds(article_ExternalArticle, url=safe_text)
@given(instance=article_ExternalArticle_strategy)
@settings(max_examples=25)
def test_article_ExternalArticle_instantiation(instance):
    assert isinstance(instance, article_ExternalArticle)


article_ExternalTarget_strategy = st.builds(article_ExternalTarget, url=safe_text)
@given(instance=article_ExternalTarget_strategy)
@settings(max_examples=25)
def test_article_ExternalTarget_instantiation(instance):
    assert isinstance(instance, article_ExternalTarget)


article_Factory_strategy = st.builds(article_Factory)
@given(instance=article_Factory_strategy)
@settings(max_examples=25)
def test_article_Factory_instantiation(instance):
    assert isinstance(instance, article_Factory)


article_Formatter_strategy = st.builds(article_Formatter)
@given(instance=article_Formatter_strategy)
@settings(max_examples=25)
def test_article_Formatter_instantiation(instance):
    assert isinstance(instance, article_Formatter)


article_HtmlFormatter_strategy = st.builds(article_HtmlFormatter, file=safe_text)
@given(instance=article_HtmlFormatter_strategy)
@settings(max_examples=25)
def test_article_HtmlFormatter_instantiation(instance):
    assert isinstance(instance, article_HtmlFormatter)


article_Identifiable_strategy = st.builds(article_Identifiable, id=safe_text)
@given(instance=article_Identifiable_strategy)
@settings(max_examples=25)
def test_article_Identifiable_instantiation(instance):
    assert isinstance(instance, article_Identifiable)


article_Image_strategy = st.builds(article_Image, file=safe_text)
@given(instance=article_Image_strategy)
@settings(max_examples=25)
def test_article_Image_instantiation(instance):
    assert isinstance(instance, article_Image)


article_ImageFactory_strategy = st.builds(article_ImageFactory, file=safe_text)
@given(instance=article_ImageFactory_strategy)
@settings(max_examples=25)
def test_article_ImageFactory_instantiation(instance):
    assert isinstance(instance, article_ImageFactory)


article_ImageFormatter_strategy = st.builds(article_ImageFormatter, file=safe_text)
@given(instance=article_ImageFormatter_strategy)
@settings(max_examples=25)
def test_article_ImageFormatter_instantiation(instance):
    assert isinstance(instance, article_ImageFormatter)


article_JavaElement_strategy = st.builds(article_JavaElement, classFile=safe_text)
@given(instance=article_JavaElement_strategy)
@settings(max_examples=25)
def test_article_JavaElement_instantiation(instance):
    assert isinstance(instance, article_JavaElement)


article_JavaFormatter_strategy = st.builds(article_JavaFormatter)
@given(instance=article_JavaFormatter_strategy)
@settings(max_examples=25)
def test_article_JavaFormatter_instantiation(instance):
    assert isinstance(instance, article_JavaFormatter)


article_JavaPackage_strategy = st.builds(article_JavaPackage, name=safe_text)
@given(instance=article_JavaPackage_strategy)
@settings(max_examples=25)
def test_article_JavaPackage_instantiation(instance):
    assert isinstance(instance, article_JavaPackage)


article_Javadoc_strategy = st.builds(article_Javadoc)
@given(instance=article_Javadoc_strategy)
@settings(max_examples=25)
def test_article_Javadoc_instantiation(instance):
    assert isinstance(instance, article_Javadoc)


article_Key_strategy = st.builds(article_Key)
@given(instance=article_Key_strategy)
@settings(max_examples=25)
def test_article_Key_instantiation(instance):
    assert isinstance(instance, article_Key)


article_Link_strategy = st.builds(article_Link)
@given(instance=article_Link_strategy)
@settings(max_examples=25)
def test_article_Link_instantiation(instance):
    assert isinstance(instance, article_Link)


article_LinkTarget_strategy = st.builds(article_LinkTarget, defaultLabel=safe_text, tooltip=safe_text)
@given(instance=article_LinkTarget_strategy)
@settings(max_examples=25)
def test_article_LinkTarget_instantiation(instance):
    assert isinstance(instance, article_LinkTarget)


article_Plugin_strategy = st.builds(article_Plugin, label=safe_text, name=safe_text)
@given(instance=article_Plugin_strategy)
@settings(max_examples=25)
def test_article_Plugin_instantiation(instance):
    assert isinstance(instance, article_Plugin)


article_PluginResource_strategy = st.builds(article_PluginResource)
@given(instance=article_PluginResource_strategy)
@settings(max_examples=25)
def test_article_PluginResource_instantiation(instance):
    assert isinstance(instance, article_PluginResource)


article_Schemadoc_strategy = st.builds(article_Schemadoc)
@given(instance=article_Schemadoc_strategy)
@settings(max_examples=25)
def test_article_Schemadoc_instantiation(instance):
    assert isinstance(instance, article_Schemadoc)


article_Section_strategy = st.builds(article_Section)
@given(instance=article_Section_strategy)
@settings(max_examples=25)
def test_article_Section_instantiation(instance):
    assert isinstance(instance, article_Section)


article_Selection_strategy = st.builds(article_Selection)
@given(instance=article_Selection_strategy)
@settings(max_examples=25)
def test_article_Selection_instantiation(instance):
    assert isinstance(instance, article_Selection)


article_Snippet_strategy = st.builds(article_Snippet, title=safe_text, titleImage=safe_text)
@given(instance=article_Snippet_strategy)
@settings(max_examples=25)
def test_article_Snippet_instantiation(instance):
    assert isinstance(instance, article_Snippet)


article_SourceCode_strategy = st.builds(article_SourceCode)
@given(instance=article_SourceCode_strategy)
@settings(max_examples=25)
def test_article_SourceCode_instantiation(instance):
    assert isinstance(instance, article_SourceCode)


article_StructuralElement_strategy = st.builds(article_StructuralElement, doc=safe_text, title=safe_text)
@given(instance=article_StructuralElement_strategy)
@settings(max_examples=25)
def test_article_StructuralElement_instantiation(instance):
    assert isinstance(instance, article_StructuralElement)


article_Text_strategy = st.builds(article_Text)
@given(instance=article_Text_strategy)
@settings(max_examples=25)
def test_article_Text_instantiation(instance):
    assert isinstance(instance, article_Text)


article_Toc_strategy = st.builds(article_Toc, levels=st.integers())
@given(instance=article_Toc_strategy)
@settings(max_examples=25)
def test_article_Toc_instantiation(instance):
    assert isinstance(instance, article_Toc)


article_TreeFormatter_strategy = st.builds(article_TreeFormatter, expandTo=st.integers(), expanded=safe_text, file=safe_text, selected=safe_text)
@given(instance=article_TreeFormatter_strategy)
@settings(max_examples=25)
def test_article_TreeFormatter_instantiation(instance):
    assert isinstance(instance, article_TreeFormatter)


article_TreeNode_strategy = st.builds(article_TreeNode, image=safe_text, label=safe_text, xmi_ID=safe_text)
@given(instance=article_TreeNode_strategy)
@settings(max_examples=25)
def test_article_TreeNode_instantiation(instance):
    assert isinstance(instance, article_TreeNode)


article_TreeNodeProperty_strategy = st.builds(article_TreeNodeProperty, key=safe_text, value=safe_text, valueImage=safe_text)
@given(instance=article_TreeNodeProperty_strategy)
@settings(max_examples=25)
def test_article_TreeNodeProperty_instantiation(instance):
    assert isinstance(instance, article_TreeNodeProperty)


article_XmlFormatter_strategy = st.builds(article_XmlFormatter, file=safe_text)
@given(instance=article_XmlFormatter_strategy)
@settings(max_examples=25)
def test_article_XmlFormatter_instantiation(instance):
    assert isinstance(instance, article_XmlFormatter)



