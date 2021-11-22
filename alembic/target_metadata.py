from bantre.modules.article import article_model
from bantre.system import user, entity, group, section
from bantre.modules.article.article_model import ArticleModel
from bantre.modules.auth.auth_model import TokenModel

target_metadata = [
    user.UserModel.metadata,
    user.UserConfigModel.metadata,
    user.users_groups.metadata,
    entity.EntityModel.metadata,
    entity.entities_sections.metadata,
    group.GroupModel.metadata,
    group.groups_sections.metadata,
    section.SectionModel.metadata,
    ArticleModel.metadata,
    TokenModel.metadata
]